"""
Biztonsági mentést készít az adatbázisról, a függvény meghívása esetén.
helye: /root/menetes
File neve tartalmazza a pontos időt, hogy mikor készült a menés ÉÉÉÉHHNNÓÓPPMM formátumban (még változhat)


Made by Gáborka in 2021
"""

def biztonsagiMentes(check = True):
    """
    A függvény amit kell kell hívni, visszatérési érték: True ha sikeres, False, ha nem a mentés
    bevett érték: check, keressen-e túl régi mentéseket amit tud törölni, True ha igen, False, ha ne
    """
    import os
    from datetime import datetime
    from shutil import copyfile
    sikeres = False
    path = 'mentes'
    try:
        os.mkdir(path)
    except FileExistsError:
        #os.chdir("mentes")
        pass
    datum = datetime.now()
    try:
        copyfile('receptek.db', '{}/{}.db'.format(path, datum.strftime("%Y%m%d%H%M%S")))
        sikeres = True
    except:
        pass


    if check:
        try:
            elemek = os.listdir(path=path)
            elemek.sort(reverse=True)
            elso = elemek[0]
            elso = int(elso[:-3])
            nap = elso - 10000000
            for i in elemek:
                if int(i[:-3]) == elemek[0]:
                    pass
                else:
                    if int(i[:-3]) < nap:
                        os.remove('{}/{}'.format(path, i))
        except:
            pass

    return sikeres


"""
Újabb dokumentáció, mert az a múltkor is nagyon bejött.
Ftp szerverre feltölti a receptek.db -t és átnevezi, majd megnézi van-e túl régi bizt mentés és azt törli.
Nem az iagz megoldás, de ehhez jó lesz, ez a MS.
Problematico vele, hogy bele van írva a host, user és a passwd azt azért valahogy megy kell oldani, mert na, de nincs ötletem utána kell nézni.
"""
def tavoli_Mentes():
    from ftplib import FTP
    from datetime import datetime
    from shutil import copyfile
    import os

    ftp = FTP(host='ftp.peter68.hu')
    ftp.login(user='kristof@peter68.hu', passwd='Kisfiam')

    ftp.cwd('recept')
    # print(ftp.pwd())
    # ftp.retrlines('LIST')

    path  = 'mentes'
    ftp.cwd(path)
    datum = datetime.now()
    file_nev = '{}.db'.format(datum.strftime("%Y%m%d%H%M%S"))
    try:
        os.mkdir('tmp')
    except:
        pass
    copyfile('receptek.db', '{}/{}'.format('tmp', file_nev))
    # ftp.sendcmd('send {}'.format(file_nev))
    # ftp.sendcmd('send 20210521120225.db')
    ftp.storbinary('STOR ' + file_nev, open('tmp/' + file_nev, 'rb'))


    elemek = ftp.nlst()
    elemek.remove('.')
    elemek.remove('..')
    elemek.sort(reverse=True)
    elso = elemek[0]
    elso = int(elso[:-3])
    nap = elso - 10000000
    for i in elemek:
        if int(i[:-3]) == elso:
            pass
        else:
            if int(i[:-3]) < nap:
                ftp.delete(i)
    
    os.remove('{}/{}'.format('tmp', file_nev))

    ftp.quit()