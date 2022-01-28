import sqlite3 as sq
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
    return keresett

def receptById(id):
    connect()
    c.execute("""SELECT * FROM receptek WHERE id LIKE ?""", ((id),))
    keresett = c.fetchone()
    return keresett