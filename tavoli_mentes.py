"""
Újabb dokumentáció, mert az a múltkor is nagyon bejött.
Ftp szerverre feltölti a receptek.db -t és aátnevezi, majd megnézi van-e túl régi bizt mentés és azt törli.
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

tavoli_Mentes()