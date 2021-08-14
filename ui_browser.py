
import sys

import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

import datetime

import database_handler
import main

elozo_oszlop = 3


def start_gui():
    global ui_browser_peldany
    root = tk.Tk()
    ui_browser_peldany = Ui_browser_class(root)
    root.mainloop()


class Ui_browser_class:

    def __init__(self, master):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        #_bgcolor = '#ff0000'  # X11 color: 'gray85'
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 11 -weight normal -slant" \
                 " roman -underline 0 -overstrike 0"
        font11 = "-family {Segoe UI} -size 12 -weight normal -slant" \
                 " roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 12 -weight normal -slant " \
                "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        # if sys.platform == "win32":
        #    self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font=("TkDefaultFont", 12))
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        #master.geometry("1000x670+150-50")
        master.geometry("956x782+461+131")
        #master.overrideredirect(False)
        #master.geometry("{0}x{1}+0+0".format(master.winfo_screenwidth()-20, master.winfo_screenheight() - 80))

        master.minsize(120, 1)
        #master.maxsize(1924, 1061)
        master.resizable(1, 1)
        master.title("Böngészés")
        master.configure(background=_bgcolor)

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)  #betűk színe
        self.style.map('TNotebook.Tab', background=[('selected', _compcolor), ('active', _ana2color)])
        self.szures = ttk.Notebook(master)
        self.szures.place(relx=0.01, rely=0.025, relheight=0.417, relwidth=0.978)
        self.szures.configure(takefocus="")

        self.szures_tab_napi = tk.Frame(self.szures)
        self.szures.add(self.szures_tab_napi, padding=3)
        self.szures.tab(0, text="Napi tucat", compound="left", underline="-1", )
        self.szures_tab_napi.configure(background=_bgcolor, highlightcolor="black")
        #background="#d9d9d9"

        self.szures_tab_alkalom = tk.Frame(self.szures)
        self.szures.add(self.szures_tab_alkalom, padding=3)
        self.szures.tab(1, text="Címke", compound="left", underline="-1", )
        self.szures_tab_alkalom.configure(background=_bgcolor)

        self.szures_tab_allergen = tk.Frame(self.szures)
        self.szures.add(self.szures_tab_allergen, padding=3)
        self.szures.tab(2, text="Allergén", compound="none", underline="-1", )
        self.szures_tab_allergen.configure(background=_bgcolor)

        self.szures_tab_osszetevo = tk.Frame(self.szures)
        self.szures.add(self.szures_tab_osszetevo, padding=3)
        self.szures.tab(3, text="Összetevő", compound="none", underline="-1", )
        self.szures_tab_osszetevo.configure(background=_bgcolor)

        self.szures_tab_forras = tk.Frame(self.szures)
        self.szures.add(self.szures_tab_forras, padding=3)
        self.szures.tab(4, text="Forrás", compound="none", underline="-1", )
        self.szures_tab_forras.configure(background=_bgcolor)


        global tabok
        tabok = {self.szures_tab_napi: ['napitucat', 'nev', 'nev'],
                 self.szures_tab_alkalom: ['alkalom', 'alkalom', 'alkalom'],
                 self.szures_tab_allergen: ['allergen_szotar', 'allergen', 'allergen'],
                 self.szures_tab_osszetevo: ['osszetevok', 'megnevezes', 'megnevezes'],
                 self.szures_tab_forras: ['receptek', 'forras', 'forras']}

        global belsotomb_osztalyok
        belsotomb_osztalyok = []  # ebbe a tömbbe kerülnek a belső tömb osztályai

        class Belso_tomb():
            '''a note füleinek belseje.'''

            def __init__(self2, tab):
                '''Belső tömbök giu leírása és függvényinek initje'''

                self2.scrollbox_list_honnan = tk.Scrollbar(tab)
                self2.scrollbox_list_honnan.place(relx=0.011+0.303, rely=0.033, relheight=0.807)
                self2.list_honnan = tk.Listbox(tab, yscrollcommand=self2.scrollbox_list_honnan.set)
                self2.list_honnan.place(relx=0.011, rely=0.033, relheight=0.807, relwidth=0.303)
                self2.list_honnan.configure(background="white", disabledforeground="#a3a3a3", font=font11,
                                           foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                           selectbackground="#c4c4c4", selectforeground="black", takefocus="0",
                                           selectmode="MULTIPLE")
                self2.list_honnan.bind('<Double-Button-1>', func=self2.button_hozzaad)
                self2.list_honnan.bind('<Return>', func=self2.button_hozzaad)
                self2.scrollbox_list_honnan.config(command=self2.list_honnan.yview)

                self2.belso_szuro = tk.Entry(tab)
                self2.belso_szuro.place(relx=0.011, rely=0.867, height=30, relwidth=0.32)
                self2.belso_szuro.configure(background="white", disabledforeground="#a3a3a3", font=font9,
                                           foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                           insertbackground="black", selectbackground="#c4c4c4",
                                           selectforeground="black", takefocus="0")
                self2.belso_szuro.bind('<KeyRelease>', self2.belso_szures_frissit)

                self2.scrollbox_list_hova = tk.Scrollbar(tab)
                self2.scrollbox_list_hova.place(relx=0.663 + 0.303, rely=0.033, relheight=0.907)
                self2.list_hova = tk.Listbox(tab, yscrollcommand=self2.scrollbox_list_hova.set)
                self2.list_hova.place(relx=0.663, rely=0.033, relheight=0.907, relwidth=0.303)
                self2.list_hova.configure(background="white", disabledforeground="#a3a3a3", font=font11,
                                         foreground="#000000", highlightbackground="#d9d9d9",
                                         highlightcolor="black", selectbackground="#c4c4c4", selectforeground="black",
                                         takefocus="0", selectmode="MULTIPLE")
                self2.list_hova.bind('<Double-Button-1>', func=self2.button_torles)
                self2.list_hova.bind('<Return>', func=self2.button_torles)
                self2.scrollbox_list_hova.config(command=self2.list_hova.yview)

                self2.btn_hozzaad = tk.Button(tab)
                self2.btn_hozzaad.place(relx=0.435, rely=0.167, height=44, width=127)
                self2.btn_hozzaad.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                                           disabledforeground="#a3a3a3", font=font9, foreground="#000000",
                                           highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                           takefocus="0", text='''Hozzáadás''', command=self2.button_hozzaad)
                self2.btn_hozzaad.bind('<Return>', func=self2.button_hozzaad)

                self2.btn_torles = tk.Button(tab)
                self2.btn_torles.place(relx=0.435, rely=0.4, height=44, width=127)
                self2.btn_torles.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                                          disabledforeground="#a3a3a3", font=font9, foreground="#000000",
                                          highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                          takefocus="0", text='''Törlés''', command=self2.button_torles)
                self2.btn_torles.bind('<Return>', func=self2.button_torles)

                self2.btn_osszes_torles = tk.Button(tab)
                self2.btn_osszes_torles.place(relx=0.435, rely=0.733, height=34, width=127)
                self2.btn_osszes_torles.configure(activebackground="#ececec", activeforeground="#000000",
                                                 background="#d9d9d9", disabledforeground="#a3a3a3",
                                                 font="-family {Segoe UI} -size 12", foreground="#000000",
                                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                                 takefocus="0", text='''Összes törlése''',
                                                 command=self2.button_osszes_torles)
                self2.btn_osszes_torles.bind('<Return>', func=self2.button_osszes_torles)

                # global tart_tomb
                self2.tart_tomb = []
                self2.listbox_honnan_tartalom = []

            def button_hozzaad(self2, event=''):
                '''Hozzáad gomb függvénye'''
                aktiv = self2.list_honnan.get('active')

                def letezik(elem):
                    '''ha létezik az elem, a fv 0-val tér vissza'''
                    if elem in self2.tart_tomb:
                        return 0
                    else:
                        return 1

                if letezik(aktiv):
                    self2.tart_tomb.append(aktiv)
                    # print(self2.tart_tomb)
                    self2.list_hova.insert('end', aktiv)
                    self.atadas()
                else:
                    print('Az elem már szerepel egyszer!')

            def button_torles(self2, event=''):
                '''Törlés gomb függvénye'''
                try:
                    aktiv = self2.list_hova.get('active')
                    self2.list_hova.delete(self2.list_hova.curselection())
                    self2.tart_tomb.remove(aktiv)
                    self.atadas()
                except:
                    print('Nincs aktív elem!')

            def button_osszes_torles(self2, event=''):
                '''Összes törlése gomb függvénye'''
                self2.list_hova.delete('0', 'end')
                self2.tart_tomb = []
                self.tree_listazas(gomb=1)

            def belso_szures_frissit(self2, event=''):
                '''a honnen tömb alatti beviteli mező hívja meg, gomb elengedésre szűri a lisbox tartalmát'''
                # jelenlegi_listbox_tartalom = self2.list_honnan.get('0', 'end')
                jelenlegi_bevitel_tartalom = self2.belso_szuro.get()
                self2.list_honnan.delete('0', 'end')
                for i in self2.listbox_honnan_tartalom:
                    if jelenlegi_bevitel_tartalom.lower() in i.lower():
                        self2.list_honnan.insert('end', i)


        def belso_tomb_letrehozas(friss=0):
            '''ez a függvény hozza létre a belső tömböt és kilistázza az adatbázisból a szűrő listákat.
            ha nincs adatbázis amiből listázni lehetne akkor a függvény amit meghív False értékkel válaszol.'''

            szamlalo = 0  # kell ez a számláló, mert így nem kell range a tabokhoz, leegyszerüsíti
            for i in tabok:
                if not friss:
                    belsotomb_osztalyok.append(Belso_tomb(i))
                kilistazott = database_handler.listazas_szurok(tabok[i])
                if kilistazott != False:
                    # belsotomb_osztalyok[szamlalo].list_honnan.delete('0', 'end')
                    belsotomb_osztalyok[szamlalo].listbox_honnan_tartalom = kilistazott
                    for j in belsotomb_osztalyok[szamlalo].listbox_honnan_tartalom:
                        if j != '':
                            belsotomb_osztalyok[szamlalo].list_honnan.insert('end', j)
                        # hozzáadja az épp aktuálisan létrehozott listához az adatbázisból listázott tételeket.
                    szamlalo += 1

        self.btn_letre = tk.Button(master)
        self.btn_letre.place(relx=0.031, rely=0.921, height=44, width=187)
        self.btn_letre.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                                 disabledforeground="#a3a3a3", font=font9, foreground="#000000",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", takefocus="0",
                                 text='''Recept létrehozás''', command=main.letrehozas_gomb)
        self.btn_letre.bind('<Return>', func=main.letrehozas_gomb)

        self.btn_megnyit = tk.Button(master)
        self.btn_megnyit.place(relx=0.774, rely=0.921, height=44, width=187)
        self.btn_megnyit.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                                   disabledforeground="#a3a3a3", font=font9, foreground="#000000",
                                   highlightbackground="#d9d9d9", highlightcolor="black", pady="0", takefocus="0",
                                   text='''Megnyitás''',
                                   command=self.recept_megnyitas_torles)
        self.btn_megnyit.bind('<Return>', func=self.recept_megnyitas_torles)

        self.btn_recept_szerk = tk.Button(master)
        self.btn_recept_szerk.place(relx=0.554, rely=0.921, height=44, width=187)
        self.btn_recept_szerk.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                                        disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 12",
                                        foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                        pady="0", takefocus="0", text='''Szerkesztés''',
                                        command=lambda: self.recept_megnyitas_torles(muvelet=2))

        self.btn_recept_torles = tk.Button(master)
        self.btn_recept_torles.place(relx=0.334, rely=0.921, height=44, width=187)
        self.btn_recept_torles.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                                         disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 12",
                                         foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                         pady="0", takefocus="0", text='''Törlés''',
                                         command=lambda: self.recept_megnyitas_torles(muvelet=1))

        self.Entry_nevkereses = tk.Entry(master)
        self.Entry_nevkereses.place(relx=0.178, rely=0.46, height=30, relwidth=0.308)
        self.Entry_nevkereses.configure(background="white", disabledforeground="#a3a3a3", font=font10,
                                        foreground="#000000", insertbackground="black", takefocus="0")
        self.Entry_nevkereses.bind('<KeyRelease>', func=lambda x: self.tree_listazas(szures=1, gomb=1))
        self.Entry_nevkereses.focus()

        self.lbl_1 = tk.Label(master)
        self.lbl_1.place(relx=0.031, rely=0.46, height=31, width=134)
        self.lbl_1.configure(background="#d9d9d9", disabledforeground="#a3a3a3", font=font9, foreground="#000000",
                             text='''Keresés névben''')

        self.bevalt_check_var = tk.IntVar()
        self.chk_bevalt = tk.Checkbutton(master)
        self.chk_bevalt.place(relx=0.502, rely=0.467, relheight=0.032, relwidth=0.181)
        self.chk_bevalt.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                                  disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 12",
                                  foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                  justify='left', text='''Csak beváltakat''',
                                  variable=self.bevalt_check_var, command=self.atadas)

        self.btn_szures_listazas = tk.Button(master)
        self.btn_szures_listazas.place(relx=0.701, rely=0.455, height=34, width=227)
        self.btn_szures_listazas.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                                           disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 12",
                                           foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                           pady="0", takefocus="0", text='''Receptek listázása''', command=self.atadas)
        self.btn_szures_listazas.bind('<Return>', func=self.atadas)

        self.oda = False

        self.scrollbar_treeview_receptek = tk.Scrollbar(master)
        self.scrollbar_treeview_receptek.place(relx=0.01+0.961, rely=0.512, relheight=0.39)

        self.treeview_receptek = ttk.Treeview(master, yscrollcommand=self.scrollbar_treeview_receptek.set)
        self.treeview_receptek.place(relx=0.01, rely=0.512, relheight=0.39, relwidth=0.961)
        self.treeview_receptek['columns'] = ('forras', 'bevalt', 'datum')
        self.treeview_receptek.column('#0', width=250)
        self.treeview_receptek.column('forras', width=150)  # 70
        self.treeview_receptek.column('bevalt', width=30)  # 70
        self.treeview_receptek.column('datum', width=50)  # 70
        self.treeview_receptek.heading('#0', text='Név', command=lambda: self.tree_listazas(oszlop=0))
        self.treeview_receptek.heading('forras', text='Forrás', command=lambda: self.tree_listazas(oszlop=1))
        self.treeview_receptek.heading('bevalt', text='Bevált?', command=lambda: self.tree_listazas(oszlop=2))
        self.treeview_receptek.heading('datum', text='Létrehozva', command=lambda: self.tree_listazas(oszlop=3))
        self.treeview_receptek.bind("<Double-1>", func=lambda x: self.recept_megnyitas_torles(muvelet=0))
        self.treeview_receptek.bind("<Return>", func=lambda x: self.recept_megnyitas_torles(muvelet=0))

        self.scrollbar_treeview_receptek.config(command=self.treeview_receptek.yview)

        belso_tomb_letrehozas()  # meghívja a belső tömböt létrehozó függvényt
        self.atadas()  # meghívja a függvényt ami kilistázza a recepteket.

    # elküldi a szűrésekest és egy tömböt vár vissza, amit utána kilistázhat.
    def atadas(self):
        '''a receptek listázása függvény hívja meg, átadja a másik fájlban lévő föggvénynek a szűrőket,
        majd meghívja a tree listázást'''

        atadando_tombok_tomb = []
        for i in belsotomb_osztalyok:
            atadando_tombok_tomb.append(i.tart_tomb)
        #print('atadando_tombok_tomb: ', atadando_tombok_tomb)

        database_handler.szures_lista(atadando_tombok_tomb, bevalt=self.bevalt_check_var.get())

        self.tree_listazas(gomb=1)

    def tree_listazas(self, oszlop=3, gomb=0, szures=0, event=''):
        """Kilistázza az elemeket. előtte törli az összes már megjelenített elemet.
        ha a szűrés paraméter 1 akkor megszűri, hogy mit listázzon ki."""

        global elozo_oszlop

        def atalakit(ertek):
            '''A bevált értékét adja vissza a tree-be íráshoz.'''
            if ertek:
                return 'Igen'
            else:
                return ''

        # ez a rész kéri le a 'gyerek' sorokat, majd ezen futtatja végig a tömböt és törli az összes elemet.
        for i in self.treeview_receptek.get_children():
            self.treeview_receptek.delete(i)

        if database_handler.recept_adat_tomb != []:

            if not gomb:
                if oszlop == elozo_oszlop:
                    self.oda = not self.oda
                else:
                    pass
                elozo_oszlop = oszlop

            #print('oszlop: ', oszlop)
            #print('adat_tomb: ', browser_handler.recept_adat_tomb)
            database_handler.recept_adat_tomb.sort(key=lambda l: l[oszlop],
                                                  reverse=self.oda)  # ha True visszafele listázza.

            for i in database_handler.recept_adat_tomb:
                if szures:
                    if self.Entry_nevkereses.get().lower() in i[0].lower():
                        self.treeview_receptek.insert("", '0', text=i[0],
                                                      values=(
                                                      i[1], atalakit(i[2]), str(datetime.datetime.fromtimestamp(i[3]))),
                                                      tags=i[3])
                else:
                    self.treeview_receptek.insert("", '0', text=i[0],
                                                  values=(
                                                  i[1], atalakit(i[2]), str(datetime.datetime.fromtimestamp(i[3]))),
                                                  tags=i[3])

    def recept_megnyitas_torles(self, muvelet=0, event=''):
        '''recept megnyitása , szerkesztése, törlése gomb függvénye
        muvelet = 0 megnyitás
        muvelet = 1 törlés
        muvelet = 2 szerkesztés'''

        database_handler.jelenlegi_tree_kijelolt = self.treeview_receptek.item(self.treeview_receptek.focus())['tags']  # [123123]
        # print('1: ', jelenlegi_tree_kijelolt)
        if database_handler.jelenlegi_tree_kijelolt != '':
            if muvelet == 1:  # törlés
                torlod = messagebox.askquestion('Recept törlése', 'Biztosan törlöd ezt a receptet?', icon='warning')
                if torlod == 'yes':
                    database_handler.recept_torles()
            elif muvelet == 2:  # szerkesztés
                database_handler.recept_megnyitas()
                main.letrehozas_gomb(szerk=1)

            else:
                main.megnyitas_gomb()

    def recept_torles_ui(self):
        torlod = messagebox.askquestion('Recept törlése', 'Biztosan törlöd ezt a receptet?', icon='warning')
        if torlod == 'yes':
            database_handler.recept_torles()
        else:
            pass


if __name__ == '__main__':
    start_gui()
