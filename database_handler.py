import sqlite3 as sq
import time

import main

#def variables():
global osszetevok_tomb
osszetevok_tomb = []
global tart_tomb
global alk_tomb
tart_tomb = []
alk_tomb = []


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


# ui_browser fv-ek

def listazas_szurok(tomb=[]):
    '''bemenetként egy tömböt kap: [tábla, oszlop, csoportosítási oszlop]
    visszatér a szűréshez szükséges kilistázott adatokkal.'''

    if not tomb:
        return print("Hibás függvénymeghívás!")
    connect()
    try:
        c.execute("""SELECT {} FROM {} GROUP BY {} ORDER BY {} ASC""".format(tomb[1], tomb[0], tomb[2], tomb[2]))
        lek_tomb = c.fetchall()
        # eredmény: [('egy',), ('ketto',)]
        lek_tomb_list = []
        for i in lek_tomb:
            lek_tomb_list.append(i[0])
        connect_close()
        return lek_tomb_list

    except:
        print("Nincs az adatbázisban adat, hozd létre az első recepted!")
        connect_close()
        return False


def szures_lista(lista_tomb=[], bevalt=0):
    '''megnyitja az adatbázist
    lekérdezi az összes recept id-ját
    ezeken végig megy, lekéri az id alapján a recept összes tulajdonságát, ezt összeveti a szűrési tömbbel
    a maradékot kinevezi összesnek és újra teszteli, hogy benne van-e a következő szűrőben.
    az utoldó szűrő után ami a tömbbe marad az a visszatérési érték.'''

    global recept_adat_tomb

    def konvert(tomb):
        '''forrás: [(1601211973,), (1604506236,)]
        eredmény: [1601211973, 1604506236]'''
        konvertalt = []
        for i in tomb:
            konvertalt.append(list(i)[0])
        # print('konvertalt: ', konvertalt)
        return konvertalt

    recept_tartalmazza = []
    connect()

    try:
        c.execute("""SELECT id, bevalt FROM receptek""")
        osszes = c.fetchall()
        # print(osszes)      #[(1605540021, 0), (1605721775, 1), (1605721918, 1)]

        if bevalt:
            for i in osszes:  # (1605540021, 0)
                if i[1]:
                    recept_tartalmazza.append(i[0])

        else:
            recept_tartalmazza = konvert(osszes)
    except:
        print('Hiba a receptek beolvasásánál! Err:browser_handler')

    # print('osszesrecept: ', recept_tartalmazza)       #pl: [1578057076, 1578057966, 1604506236, 1604602727]

    if lista_tomb[0] != []:  # csak akkor kell a szűrés, ha a szűrő nem üres!
        osszesrecept = recept_tartalmazza
        recept_tartalmazza = []
        for i in osszesrecept:
            # print('aktualis recept: ', i)
            osszes_volt = True  # feltételezzük, hogy benne van, akkor állítja át, ha nincs benne
            c.execute("""SELECT tartalom FROM tartalom WHERE id = {}""".format(i))
            # lekérdezi az összes recept tartalmát
            tartalom_kilistazott = c.fetchall()
            # print('tartalom_kilistazott(tartalom): ', tartalom_kilistazott)
            for j in lista_tomb[0]:  # végig megy a szűrő tömbön.
                # print('lista_tomb aktuálisa: ', j)
                if j not in konvert(
                        tartalom_kilistazott):  # ha a szűrő eleme nincs benne a recept össze lekrdezettjében, nem tartalmazza.
                    # print('nincs benne')
                    osszes_volt = False
                    break  # tovább lép a következő receptre, nézi a következő id-t
            if osszes_volt:
                recept_tartalmazza.append(i)
                # print('tartalmazza az összeset.')

            # print('1: ', recept_tartalmazza)

    if lista_tomb[1] != []:  # csak akkor kell a szűrés, ha a szűrő nem üres!
        if recept_tartalmazza != []:
            osszesrecept = recept_tartalmazza
            recept_tartalmazza = []
            for i in osszesrecept:
                osszes_volt = True
                if osszesrecept != []:
                    c.execute("""SELECT alkalom FROM alkalom WHERE id = {}""".format(i))
                    tartalom_kilistazott = c.fetchall()
                    # print('tartalom_kilistazott(alkalom): ', tartalom_kilistazott)
                    for j in lista_tomb[1]:
                        if j not in konvert(tartalom_kilistazott):
                            osszes_volt = False
                            break
                    if osszes_volt:
                        recept_tartalmazza.append(i)
            # print('2: ', recept_tartalmazza)

    if lista_tomb[3] != []:  # csak akkor kell a szűrés, ha a szűrő nem üres!
        if recept_tartalmazza != []:
            osszesrecept = recept_tartalmazza
            recept_tartalmazza = []
            for i in osszesrecept:
                osszes_volt = True
                if osszesrecept != []:
                    c.execute("""SELECT megnevezes FROM osszetevok WHERE id = {}""".format(i))
                    tartalom_kilistazott = c.fetchall()
                    # print('tartalom_kilistazott(osszetevok): ', tartalom_kilistazott)
                    for j in lista_tomb[3]:
                        if j not in konvert(tartalom_kilistazott):
                            osszes_volt = False
                            break
                    if osszes_volt:
                        recept_tartalmazza.append(i)
            # print('3: ', recept_tartalmazza)

    if lista_tomb[2] != []:  # csak akkor kell a szűrés, ha a szűrő nem üres!
        if recept_tartalmazza != []:
            osszesrecept = recept_tartalmazza
            recept_tartalmazza = []
            for i in osszesrecept:
                osszes_volt = True
                if osszesrecept != []:
                    c.execute("""SELECT allergen FROM allergen_szotar WHERE hozzavalo in
                        (SELECT megnevezes FROM osszetevok WHERE id = {})""".format(i))
                    # az allergéneket a hozzávalók alapján kell kikeresni, ez munkaigéényesebb, ezért ez lesz az utolsó lépés!
                    tartalom_kilistazott = c.fetchall()
                    # print('tartalom_kilistazott(allergen): ', tartalom_kilistazott)
                    for j in lista_tomb[2]:
                        if j not in konvert(tartalom_kilistazott):
                            osszes_volt = False
                            break
                    if osszes_volt:
                        recept_tartalmazza.append(i)
            # print('3: ', recept_tartalmazza)

    if lista_tomb[4] != []:  # csak akkor kell a szűrés, ha a szűrő nem üres!
        if recept_tartalmazza != []:
            osszesrecept = recept_tartalmazza
            recept_tartalmazza = []
            for i in osszesrecept:
                osszes_volt = True
                if osszesrecept != []:
                    c.execute("""SELECT forras FROM receptek WHERE id = {}""".format(i))
                    tartalom_kilistazott = c.fetchall()
                    # print('tartalom_kilistazott(forras): ', tartalom_kilistazott)
                    for j in lista_tomb[4]:
                        if j not in konvert(tartalom_kilistazott):
                            osszes_volt = False
                            break
                    if osszes_volt:
                        recept_tartalmazza.append(i)

    recept_adat_tomb = []

    for i in recept_tartalmazza:
        try:
            c.execute("""SELECT nev, forras, bevalt, id FROM receptek WHERE id={}""".format(i))
            recept_adatok = c.fetchall()  # pl: [('Példa recept', forras, bevalt, id)] nem aktuális
            for i in recept_adatok:
                recept_adat_tomb.append(list(i))  # pl: [['uj recept', forras, id], ['Példa recept', 20]] nem aktuális
        except:
            print("Hiba történt a legkérdezés közben! Err:browser_handler.szures_lista_2")

    connect_close()


# ui_view fv-ek

global jelenlegi_tree_kijelolt


def recept_torles():
    recept_id = jelenlegi_tree_kijelolt[0]
    tablak = ['alkalom', 'osszetevok', 'receptek', 'tartalom']

    connect()

    for i in tablak:
        c.execute("""DELETE FROM {} WHERE id = {}""".format(i, recept_id))

    conn.commit()
    connect_close()


def recept_megnyitas():
    '''global változóból: id alapján lekéri az összes kilistázandó adatot az adatbázisból.
    az összegyűjtött adatokat global változókba menti
    a visszatérési érték eredményes futás esetén: 1'''

    global recept_adatok_recept
    global recept_adatok_osszetevok
    global recept_adatok_alkalom
    global recept_adatok_tartalom

    # recept_id: browser_ui.jelenlegi_tree_kijelolt

    if jelenlegi_tree_kijelolt != []:
        recept_id = jelenlegi_tree_kijelolt[0]

        connect()

        c.execute("""SELECT nev, elkeszites, ido, forras, bevalt, adag, adag_me FROM receptek WHERE id={}""".format(
            recept_id))
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

        return 1

    else:
        print('Nincs recept kiválasztva!')
        return 0


# add_ui fv-ek

def forras_kitalalas():
    connect()
    # print("megnyitva")

    global eredmeny_forras
    eredmeny_forras = []

    try:
        c.execute("SELECT forras FROM receptek GROUP BY forras ORDER BY count(forras) DESC")
        eredmeny = c.fetchall()  # [('',), ('forrás',), ('uresddde',)]

    except:
        pass
    connect_close()

    if eredmeny != []:
        for i in eredmeny:
            if i != '':
                eredmeny_forras.append(i[0])


def osszetevok_fugg(megnevezes, mennyiseg, me, index='end'):
    """gui hívja meg, átadja az adatokat, a függvény hozzáadja egy tömbhöz(2d!).
    ez a tömb fogja tartalmazni az adatokat amiket átad a progaram a Recept oztály számára."""

    if index == 'end':
        index = len(osszetevok_tomb)

    osszetevok_tomb.insert(index, [megnevezes, mennyiseg, me])


def tovabb_gomb_fugg(nev='', ido=0, elkeszites='', adag='', adag_me='', bevalt=0, forras='', szerk=0):
    """A kész gomb függvénye, a gui-tól kapja az adatokat, tömbbe rendezi amit majd átad a Recept osztálynak"""
    global alapadatok
    alapadatok = [nev, ido, elkeszites, adag, adag_me, forras, bevalt]

    recept_osztaly_adatbev(szerk=szerk)


def torles_fugg(elem):
    osszetevok_tomb.remove(osszetevok_tomb[elem])


def recept_osztaly_letre():
    global recept
    recept = Recept()
    recept.connect()
    recept.tablak_letrehozasa()


def recept_osztaly_adatbev(szerk=0):
    # alapadatok = [nev, ido, elkeszites, bevalt]
    # osszetevok_tomb = [megnevezes, mennyiseg, me]
    recept.adat_hozzaadas(alapadatok=alapadatok, osszetevok=osszetevok_tomb)
    recept.adatok_bevitele(szerk=szerk)


def mertekegyseg_kitalalas(hozzavalo):
    connect()
    # print("megnyitva")
    try:
        c.execute(
            "SELECT mertekegyseg, count(mertekegyseg) FROM osszetevok WHERE megnevezes = '{}' GROUP BY mertekegyseg ORDER BY count(mertekegyseg) DESC".format(
                hozzavalo))
        eredmeny_me = c.fetchall()  # pl.: [('db', 1)]

        connect_close()
    except:
        connect_close()
        return ''

    if eredmeny_me == []:
        return ''
    else:
        return eredmeny_me[0][0]


# ui_category fv-ek:

def szerk_listazas():
    '''Szerkesztés esetén a listbe listázáshoz készít elő és így nem kell a guiból még egyet importolni.'''
    # view_handler.recept_adatok_alkalom  # pl: [('egyik',), ('masik',), ('harmadik',)]
    # view_handler.recept_adatok_tartalom  # pl: [('Egyéb zöldségek',), ('Egyéb gyümölcsök',), ('Bogyós gyümölcsök',)]

    global alkalom_listazas_tomb
    global tartalom_listazas_tomb

    alkalom_listazas_tomb = []
    tartalom_listazas_tomb = []

    for i in recept_adatok_alkalom:
        alkalom_listazas_tomb.append(i[0])
    for i in recept_adatok_tartalom:
        tartalom_listazas_tomb.append(i[0])


def alk_tart_lekerdezes(tabla, oszlop):
    connect()
    c.execute("""SELECT {} FROM {} GROUP BY {}""".format(oszlop, tabla, oszlop))
    lek_tomb = c.fetchall()
    # eredmény: [('egy',), ('ketto',)]
    for i in range(len(lek_tomb)):
        lek_tomb[i] = lek_tomb[i][0]
    connect_close()
    lek_tomb.sort()
    return lek_tomb


def kesz_gomb_fugg():
    alk_tomb.sort()
    tart_tomb.sort()
    recept.alk_tart_hozzaadas(alk_tomb, tart_tomb)
    recept.connect_close()
    main.bizt_mentes()


# recept osztaly:

class Recept():

    def __init__(self):
        pass

    def connect(self):
        """megnyitja az adatbázist és megnyitja a kurzort."""

        self.conn = sq.connect('receptek.db')
        # conn = sq.connect(':memory:')
        self.c = self.conn.cursor()

    def connect_close(self):
        """Bezárja a kurzort és az adatbázist."""
        self.c.close()
        self.conn.close()

    def tablak_letrehozasa(self):
        """Létrehozza a táblákat, ha még nem léteznek."""

        self.c.execute("""CREATE TABLE IF NOT EXISTS receptek (
                    id INTEGER,
                    nev TEXT,
                    elkeszites TEXT,
                    ido INT,
                    adag TEXT,
                    adag_me TEXT,
                    forras TEXT,
                    bevalt BOOLEAN
                    ) """)
        self.c.execute("""CREATE TABLE IF NOT EXISTS osszetevok (
                    id INTEGER,
                    megnevezes TEXT,
                    mennyiseg TEXT,
                    mertekegyseg TEXT
                    ) """)
        self.c.execute("""CREATE TABLE IF NOT EXISTS alkalom (
                    id INTEGER,
                    alkalom TEXT
                    ) """)
        self.c.execute("""CREATE TABLE IF NOT EXISTS tartalom (
                    id INTEGER,
                    tartalom TEXT
                    ) """)
        self.c.execute("""CREATE TABLE IF NOT EXISTS allergen_szotar (
                    hozzavalo TEXT,
                    allergen TEXT
                    ) """)
        self.c.execute("""CREATE TABLE IF NOT EXISTS allergen_recept (
                    id INTEGER,
                    nev TEXT
                    ) """)
        self.c.execute("""CREATE TABLE IF NOT EXISTS napitucat (
                    nev TEXT
                    ) """)
        self.c.execute("""SELECT * FROM napitucat""")
        if self.c.fetchall() == []:
            napitucat_tomb = ['Babfélék', 'Bogyós gyümölcsök', 'Egyéb gyümölcsök', 'Keresztes virágúak',
                              'Zöld levelesek', 'Egyéb zöldségek', 'Lenmag', 'Magyvak és diófélék',
                              'Fűszerek, Gyógynövények', 'Teljes kiőrlésű gabonafélék']

            for i in napitucat_tomb:
                self.c.execute("""INSERT INTO napitucat (nev) VALUES (?)""", [i])

    def alk_tart_hozzaadas(self, alkalom=[], tartalom=[]):
        # print('alk_tart')
        self.alkalom = alkalom
        self.tartalom = tartalom

        if self.szerk:
            self.c.execute("""DELETE FROM alkalom WHERE id={}""".format(recept_id))
            self.c.execute("""DELETE FROM tartalom WHERE id={}""".format(recept_id))

        # alkalom táblába felvétel: id, alkalom
        for i in self.alkalom:
            self.c.execute("""INSERT INTO alkalom (id, alkalom) VALUES (?, ?)""", (recept_id, i))

        # tartalom táblába felvétel: id, tartalom

        for i in self.tartalom:
            self.c.execute("""INSERT INTO tartalom (id, tartalom) VALUES (?, ?)""", (recept_id, i))

        self.conn.commit()

        # print('Adatok bevitele sikeres!')

    def adat_hozzaadas(self, alapadatok, osszetevok):
        '''alapadatok: [nev, ido, elkeszites, bevalt]'''
        self.nev = alapadatok[0]
        self.elkeszites = alapadatok[2]
        self.ido = alapadatok[1]
        self.adag = alapadatok[3]
        self.adag_me = alapadatok[4]
        self.forras = alapadatok[5]
        self.bevalt = alapadatok[6]
        self.osszetevok = osszetevok

    def adatok_bevitele(self, szerk=0):
        """Adatok felvitele az adatbázisba, a megfelelő táblába"""
        # recept táblába felvitel: id, név, elkészítés, idő
        global recept_id
        self.szerk = szerk

        if not self.szerk:
            # generál egy id-t a recepthez, megnézi, hgy van-e már ilyne nevű az adatbázisban és addig generál amíg olyat nem talál ami nem foglalt.
            while True:
                recept_id = int(time.time())
                self.c.execute("SELECT id FROM receptek WHERE id = {}".format(recept_id))
                if len(self.c.fetchall()) == 0:
                    break
            self.c.execute(
                "INSERT INTO receptek (id, nev, elkeszites, ido, adag, adag_me, forras, bevalt) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                (recept_id, self.nev, self.elkeszites, self.ido, self.adag, self.adag_me, self.forras, self.bevalt))

            # osszetevok táblába felvétel: id, megnevezes, mennyiseg, mertekegyseg

        else:
            recept_id = jelenlegi_tree_kijelolt[0]
            self.c.execute(
                """UPDATE receptek SET nev='{}', elkeszites='{}', ido='{}', adag='{}', adag_me='{}', forras='{}', bevalt='{}' WHERE id='{}'""".format(
                    self.nev,
                    self.elkeszites,
                    self.ido,
                    self.adag,
                    self.adag_me,
                    self.forras,
                    self.bevalt,
                    recept_id))
            self.c.execute("""DELETE FROM osszetevok WHERE id='{}'""".format(recept_id))
            self.conn.commit()

        for i in self.osszetevok:
            self.c.execute(
                """INSERT INTO osszetevok (id, megnevezes, mennyiseg, mertekegyseg) 
                VALUES ('{}', '{}', '{}', '{}')""".format(recept_id, i[0], i[1],
                                                          i[2]))  # nem tudsz aposztrófos összetevőt hozzáadni...

        self.conn.commit()
        self.osszetevok = []


if __name__ == '__main__':
    pass
