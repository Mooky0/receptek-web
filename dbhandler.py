import sqlite3 as sq
from ssl import OP_NO_RENEGOTIATION

from app import recept
#import time

global szurok

def connect():
    '''megnyitja az adatbázist és megnyitja a kurzort.'''
    global conn
    global c

    try:
        conn = sq.connect('receptek.db')
        # conn = sq.connect(':memory:')
        c = conn.cursor()
        # print("Kapcsolat megnyitva!(browser)")
    except:
        pass
        # print("Hiba az adatbázis létrehozásakor!")


def connect_close():
    '''Bezárja a kurzort és az adatbázist.'''
    try:
        c.close()
        conn.close()
    except:
        pass

def init_lista():
    szurok = [["Napi tucat"], ["Cimke"], ["Allergén"], ["Összetevők"], ["Forrás"]]

    ## Napi tucat:
    connect()
    c.execute("SELECT nev FROM napitucat")
    napitucat = c.fetchall()
    napitucatKi = []
    for i in napitucat:
        if i[0] not in napitucatKi:
            napitucatKi.append(i[0])
    szurok[0].append(len(napitucat))
    szurok[0].append(napitucatKi)

    ## Cimke:
    c.execute("SELECT alkalom FROM alkalom")
    alkalom = c.fetchall()
    alkalomKi = []
    for i in alkalom:
        if i[0] not in alkalomKi:
            alkalomKi.append(i[0])
    szurok[1].append(len(alkalomKi))
    szurok[1].append(alkalomKi)

    ## Allergén
    ## ?
    szurok[2].append(0)
    szurok[2].append([])

    ## Összetevők:
    c.execute("SELECT megnevezes FROM osszetevok")
    osszetevok = c.fetchall()
    osszetevokKi = []
    for i in osszetevok:
        if i[0] not in osszetevokKi:
            osszetevokKi.append(i[0])
    szurok[3].append(len(osszetevokKi))
    szurok[3].append(osszetevokKi)

    ## Forras:
    c.execute("SELECT forras FROM receptek")
    forras = c.fetchall()
    forrasKi = []
    for i in forras:
        if i[0] not in forrasKi:
            forrasKi.append(i[0])
    szurok[4].append(len(forrasKi))
    szurok[4].append(forrasKi)
    
    #print(szurok)
    connect_close()
    return szurok

def kereso(kereses):
    connect()
    c.execute("""SELECT * FROM receptek WHERE nev LIKE ?""",  (('%' + kereses + '%'),))
    keresett = c.fetchall()
    connect_close()
    return keresett

def receptById(recept_id):
    connect()
    # c.execute("""SELECT * FROM receptek WHERE id LIKE ?""", ((id),))
    # keresett = c.fetchone()
    # connect()

    recept_adatok_recept = []
    recept_adatok_osszetevok =  []
    recept_adatok_alkalom = []
    recept_adatok_tartalom = []


    c.execute("""SELECT id, nev, elkeszites, ido, forras, bevalt, adag, adag_me FROM receptek WHERE id={}""".format(recept_id))
    recept_adatok_recept = c.fetchall()  # pl: [('Példa recept', 'leírás', 20, forras, 0)]
    # print(recept_adatok_recept)
    c.execute("""SELECT megnevezes, mennyiseg, mertekegyseg FROM osszetevok WHERE id={}""".format(recept_id))
    recept_adatok_osszetevok = c.fetchall()  # pl: [('Tojás', 3.0, 'db'), ('Káposzta', 'fél', 'fej'), ('Liszt', 1.0, 'bögre')]
    # print(recept_adatok_osszetevok)

    c.execute("""SELECT alkalom FROM alkalom WHERE id={}""".format(recept_id))
    recept_adatok_alkalom = c.fetchall()  # pl: [('egyik',), ('masik',), ('harmadik',)]

    c.execute("""SELECT tartalom FROM tartalom WHERE id={}""".format(recept_id))
    recept_adatok_tartalom = c.fetchall()  # pl: [('Egyéb zöldségek',), ('Egyéb gyümölcsök',), ('Bogyós gyümölcsök',)]

    connect_close()
    if recept_adatok_recept == [] or recept_adatok_recept == None:
        return None
    
    keresett = {
        "adatok": recept_adatok_recept,
        "len_adatok": len(recept_adatok_recept),
        "osszetevok": recept_adatok_osszetevok,
        "len_osszetevok": len(recept_adatok_osszetevok),
        "alkalom": recept_adatok_alkalom,
        "len_alkalom": len(recept_adatok_alkalom),
        "tartalom": recept_adatok_tartalom,
        "len_tartalom": len(recept_adatok_tartalom)
    }
    # print(keresett)
    return keresett

def konvert(tomb):
    vissza = []
    for i in tomb:
        vissza.append(i[0])
    return vissza

def receptById_csakNevek(recept_id):
    connect()
    # c.execute("""SELECT * FROM receptek WHERE id LIKE ?""", ((id),))
    # keresett = c.fetchone()
    # connect()

    recept_adatok_osszetevok =  []
    recept_adatok_alkalom = []
    recept_adatok_tartalom = []

    c.execute("""SELECT megnevezes FROM osszetevok WHERE id={}""".format(recept_id))
    recept_adatok_osszetevok = c.fetchall()  # pl: [('Tojás',), ('Káposzta',), ('Liszt',)]
    # print(recept_adatok_osszetevok)
    recept_adatok_osszetevok = konvert(recept_adatok_osszetevok)

    c.execute("""SELECT alkalom FROM alkalom WHERE id={}""".format(recept_id))
    recept_adatok_alkalom = c.fetchall()  # pl: [('egyik',), ('masik',), ('harmadik',)]
    recept_adatok_alkalom = konvert(recept_adatok_alkalom)

    c.execute("""SELECT tartalom FROM tartalom WHERE id={}""".format(recept_id))
    recept_adatok_tartalom = c.fetchall()  # pl: [('Egyéb zöldségek',), ('Egyéb gyümölcsök',), ('Bogyós gyümölcsök',)]
    recept_adatok_tartalom = konvert(recept_adatok_tartalom)
    
    c.execute("""SELECT forras FROM receptek WHERE id={}""".format(recept_id))
    recept_adatok_forras = c.fetchall()
    recept_adatok_forras = konvert(recept_adatok_forras )

    keresett = {
        "osszetevok": recept_adatok_osszetevok,
        "alkalom": recept_adatok_alkalom,
        "tartalom": recept_adatok_tartalom,
        "forras": recept_adatok_forras
    }

    return keresett

def szures(tags):
    """A teg-ekből leszűri az adatbázist."""

    if tags == []:
        return None

    connect()
    # Az összes recept id és eváltságának kiszedése
    c.execute("""SELECT id, bevalt FROM receptek""")
    osszes = c.fetchall()
    # print(osszes)      Out: [(1605540021, 0), (1605721775, 1), (1605721918, 1)]

    bevalt_tomb = []
    # Leszűjük ami nem vált be.
    for i in osszes:
        if(i[1] == 1):
            bevalt_tomb.append(i[0])

    leszurt = []
    # Egyesével végigmegyünk
    for tag in tags:
        for i in bevalt_tomb:
            recept = receptById_csakNevek(i)
            # print(recept["osszetevok"])
            if tag in recept["osszetevok"] or tag in recept["alkalom"] or tag in recept["tartalom"] or tag in recept["forras"]:
                [leszurt.append(i) if i not in leszurt else leszurt]

    return leszurt

def lista(ids):
    receptek = []
    for i in ids:
        recept = receptById(i)
        receptek.append(recept)
    return receptek