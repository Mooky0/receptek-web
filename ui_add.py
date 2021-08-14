#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#

import sys

import tkinter as tk
import tkinter.ttk as ttk

import database_handler
import main

py3 = True


def destroy_window():
    pass

def vp_start_gui(szerk=0):
    '''Starting point when module is the main routine.'''
    global ui_add_peldany
    global root
    root = tk.Tk()
    ui_add_peldany = ujrecept(root, szerk=szerk)
    root.mainloop()


# bevalt_check_var = tk.IntVar()

#cim_var = tk.StringVar()

class ujrecept:
    def __init__(self, master=None, szerk=0):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''

        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        # if sys.platform == "win32":
        #    self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        if szerk:
            cim = 'Recept szerkesztése'
        else:
            cim = 'Új recept'

        master.geometry("678x514+400+75")
        master.minsize(600, 450)
        master.maxsize(1370, 749)
        master.resizable(1, 1)
        master.title(cim)
        master.configure(background="#efefef", highlightbackground="#d9d9d9", highlightcolor="black")

        self.cim = tk.Label(master)
        self.cim.configure(activebackground="#f9f9f9", activeforeground="black", anchor='w', background="#efefef",
                           disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 24",
                           foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", text=str(cim))
        self.cim.place(relx=0.044, rely=0.039, height=41, width=350)

        self.Frame1 = tk.Frame(master)
        self.Frame1.place(relx=0.044, rely=0.156, relheight=0.807, relwidth=0.465)
        self.Frame1.configure(relief='groove', borderwidth="2", background="#efefef", highlightbackground="#d9d9d9",
                              highlightcolor="black")

        self.rec_nev = tk.Label(self.Frame1)
        self.rec_nev.place(relx=0.032, rely=0.022, height=21, width=92)
        self.rec_nev.configure(activebackground="#f9f9f9", activeforeground="black", anchor='w', background="#efefef",
                               disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9",
                               foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                               text='''Név:''')

        self.rec_ido = tk.Label(self.Frame1)
        self.rec_ido.place(relx=0.032, rely=0.095, height=21, width=109)
        self.rec_ido.configure(activebackground="#f9f9f9", activeforeground="black", anchor='w', background="#efefef",
                               disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9",
                               foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                               text='''Elkészítési idõ:''')

        self.rec_hozz = tk.Label(self.Frame1)
        self.rec_hozz.place(relx=0.032, rely=0.167, height=21, width=89)
        self.rec_hozz.configure(activebackground="#f9f9f9", activeforeground="black", anchor='w', background="#efefef",
                                disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9",
                                foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                text='''Hozzávalók''')

        self.hozz_nev = tk.Label(self.Frame1)
        self.hozz_nev.place(relx=0.063, rely=0.239, height=21, width=29)
        self.hozz_nev.configure(activebackground="#f9f9f9", activeforeground="black", anchor='w', background="#efefef",
                                disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9",
                                foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                text='''Név:''')

        self.hozz_menny = tk.Label(self.Frame1)
        self.hozz_menny.place(relx=0.063, rely=0.311, height=21, width=79)
        self.hozz_menny.configure(activebackground="#f9f9f9", activeforeground="black", anchor='w',
                                  background="#efefef", disabledforeground="#a3a3a3",
                                  font="-family {Segoe UI} -size 9", foreground="#000000",
                                  highlightbackground="#d9d9d9", highlightcolor="black", text='''Mennyiség:''')

        self.hozz_me = tk.Label(self.Frame1)
        self.hozz_me.place(relx=0.603, rely=0.311, height=21, width=39)
        self.hozz_me.configure(activebackground="#f9f9f9", activeforeground="black", anchor='w', background="#efefef",
                               disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9",
                               foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                               text='''Me.:''')

        self.lbl_adag = tk.Label(self.Frame1)
        self.lbl_adag.place(relx=0.032, rely=0.384, height=21, width=39)
        self.lbl_adag.configure(activebackground="#f9f9f9", activeforeground="black", anchor='w', background="#efefef",
                               disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9",
                               foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                               text='''Adag:''')

        adaglist = ['-', '0.5']
        for i in range(1, 101): adaglist.append(str(i))

        self.spnbox_adag = tk.Spinbox(self.Frame1)
        self.spnbox_adag.place(relx=0.170, rely=0.384, height=21, width=39)
        self.spnbox_adag.configure(activebackground="#f9f9f9", background="#ffffff",
                                font="-family {Segoe UI} -size 9",
                                foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                values=tuple(adaglist))

        self.Entry_adag_me = tk.Entry(self.Frame1)
        self.Entry_adag_me.place(relx=0.317, rely=0.384, height=20, relwidth=0.180)
        self.Entry_adag_me.configure(background="white", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                                   foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                   insertbackground="black", selectbackground="#c4c4c4", selectforeground="black")

        self.rec_elk = tk.Label(self.Frame1)
        self.rec_elk.place(relx=0.032, rely=0.456, height=21, width=79)
        self.rec_elk.configure(activebackground="#f9f9f9", activeforeground="black", anchor='w', background="#efefef",
                               disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9",
                               foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                               text='''Elkészítés:''')

        self.bevalt_check_var = tk.IntVar()
        self.bevalt_check_var.set(0)
        self.chk_bevalt = tk.Checkbutton(self.Frame1)
        self.chk_bevalt.place(relx=0.508, rely=0.456, height=21, width=128)
        self.chk_bevalt.configure(activebackground="#ececec", activeforeground="#000000", background="#efefef",
                                  disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                                  foreground="#000000",
                                  highlightbackground="#d9d9d9", highlightcolor="black", justify='left',
                                  text='''Ez bevált recept''',
                                  command=lambda: self.bevalt_check_var.set(not self.bevalt_check_var.get()))

        self.Entry_nev = tk.Entry(self.Frame1)
        self.Entry_nev.place(relx=0.159, rely=0.022, height=20, relwidth=0.775)
        self.Entry_nev.configure(background="white", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                                 foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                 insertbackground="black", selectbackground="#c4c4c4", selectforeground="black")
        self.Entry_nev.focus()

        self.Entry_ido = tk.Entry(self.Frame1)
        self.Entry_ido.place(relx=0.349, rely=0.095, height=20, relwidth=0.425)
        self.Entry_ido.configure(background="white", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                                 foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                 insertbackground="black", selectbackground="#c4c4c4", selectforeground="black")

        self.Entry_hozz_nev = tk.Entry(self.Frame1)
        self.Entry_hozz_nev.place(relx=0.222, rely=0.239, height=20, relwidth=0.711)
        self.Entry_hozz_nev.configure(background="white", disabledforeground="#a3a3a3",
                                      font="-family {Segoe UI} -size 10",
                                      foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                      insertbackground="black", selectbackground="#c4c4c4", selectforeground="black")
        self.Entry_hozz_nev.bind('<Return>', func=self.osszetevok_hozz_gui)
        self.Entry_hozz_nev.bind('<FocusOut>', func=self.me_kereses)

        self.Entry_menny = tk.Entry(self.Frame1)
        self.Entry_menny.place(relx=0.317, rely=0.311, height=20, relwidth=0.235)
        self.Entry_menny.configure(background="white", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                                   foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                   insertbackground="black", selectbackground="#c4c4c4", selectforeground="black")
        self.Entry_menny.bind('<Return>', func=self.osszetevok_hozz_gui)

        self.Entry_forras = tk.Entry(self.Frame1)
        self.Entry_forras.place(relx=0.169, rely=0.935, height=20, relwidth=0.765)
        self.Entry_forras.configure(background="white", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                                 foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                 insertbackground="black", selectbackground="#c4c4c4", selectforeground="black")
        self.Entry_forras.bind('<KeyRelease>', self.forras_kitalal)


        self.rec_forras = tk.Label(self.Frame1)
        self.rec_forras.place(relx=0.032, rely=0.935, height=20, relwidth=0.125)
        self.rec_forras.configure(activebackground="#f9f9f9", activeforeground="black", anchor='w', background="#efefef",
                               disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 9",
                               foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                               text='''Forrás:''')

        self.scrollbar_txt_elk = tk.Scrollbar(self.Frame1)
        self.scrollbar_txt_elk.place(relx=0.032+0.885, rely=0.528, relheight=0.395)
        self.txt_elk = tk.Text(self.Frame1, yscrollcommand=self.scrollbar_txt_elk.set)
        self.txt_elk.place(relx=0.032, rely=0.528, relheight=0.395, relwidth=0.885)
        self.txt_elk.configure(background="white", font="-family {Segoe UI} -size 10", foreground="black",
                               highlightbackground="#d9d9d9",
                               highlightcolor="black", insertbackground="black", selectbackground="#c4c4c4",
                               selectforeground="black", wrap="word")
        self.scrollbar_txt_elk.config(command=self.txt_elk.yview)

        self.btn_hozz = tk.Button(self.Frame1)
        self.btn_hozz.place(relx=0.540, rely=0.380, height=24, width=122)
        self.btn_hozz.configure(activebackground="#ececec", activeforeground="#000000", background="#ffffff",
                                disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                highlightcolor="black", pady="0", text='''Hozzávaló hozzáadása''')
        self.btn_hozz.configure(command=self.osszetevok_hozz_gui)
        self.btn_hozz.bind('<Return>', func=self.osszetevok_hozz_gui)

        self.Entry_me = tk.Entry(self.Frame1)
        self.Entry_me.place(relx=0.73, rely=0.311, height=20, relwidth=0.203)
        self.Entry_me.configure(background="white", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                                foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                insertbackground="black", selectbackground="#c4c4c4", selectforeground="black")
        self.Entry_me.bind('<Return>', func=self.osszetevok_hozz_gui)

        self.Label_perc = tk.Label(self.Frame1)
        self.Label_perc.place(relx=0.794, rely=0.095, height=21, width=39)
        self.Label_perc.configure(activebackground="#f9f9f9", activeforeground="black", background="#efefef",
                                  disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                  highlightcolor="black", text='''perc''')

        self.btn_tovabb = tk.Button(master)
        self.btn_tovabb.place(relx=0.634, rely=0.856, height=44, width=147)
        self.btn_tovabb.configure(activebackground="#ececec", activeforeground="#000000", background="#ffffff",
                                  disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                  highlightcolor="black", pady="0", text='''Tovább''')
        self.btn_tovabb.configure(command=lambda: self.tovabb_gomb_gui(szerk=szerk))
        self.btn_tovabb.bind('<Return>', func=lambda: self.tovabb_gomb_gui(szerk=szerk))

        self.message = tk.Listbox(master)
        self.message.place(relx=0.546, rely=0.156, relheight=0.574, relwidth=0.395)
        self.message.configure(background="white", disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 10",
                               foreground="black",
                               highlightbackground="#d9d9d9", highlightcolor="#d9d9d9", selectbackground="#c4c4c4",
                               selectforeground="black")

        self.btn_fel = tk.Button(master)
        self.btn_fel.place(relx=0.955, rely=0.156, height=140, width=20)
        self.btn_fel.configure(activebackground="#ececec", activeforeground="#000000", background="#ffffff",
                                  disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                  highlightcolor="black", pady="0", text='''F''', command=lambda: self.mozgatas(irany=1))

        self.btn_le = tk.Button(master)
        self.btn_le.place(relx=0.955, rely=0.455, height=140, width=20)
        self.btn_le.configure(activebackground="#ececec", activeforeground="#000000", background="#ffffff",
                                  disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                  highlightcolor="black", pady="0", text='''L''', command=lambda: self.mozgatas(irany=2))

        self.btn_torles = tk.Button(master)
        self.btn_torles.place(relx=0.9, rely=0.759, height=24, width=42)
        self.btn_torles.configure(activebackground="#ececec", activeforeground="#000000", background="#ffffff",
                                  disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                  highlightcolor="black", pady="0", text='''Törlés''')
        self.btn_torles.configure(command=lambda: self.torles_szerkesztes_gomb_gui(szerk_gomb=0))

        self.btn_szerkeszt = tk.Button(master)
        self.btn_szerkeszt.place(relx=0.782, rely=0.759, height=24, width=67)
        self.btn_szerkeszt.configure(activebackground="#ececec", activeforeground="#000000", background="#ffffff",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", pady="0", text='''Szerkesztés''')
        self.btn_szerkeszt.configure(command=lambda: self.torles_szerkesztes_gomb_gui(szerk_gomb=1))

        database_handler.osszetevok_tomb = []
        database_handler.forras_kitalalas()       #database_handler.eredmeny_forras

        self.szerk_gomb = 0     #változó létrehozása, alapérték beállítás

        if szerk:
            # print('szerk: ', szerk)
            # pl: [('Példa recept', 'leírás', 20, 0)]
            #view_handler.recept_adatok_recept[0]
            self.Entry_nev.insert('0', database_handler.recept_adatok_recept[0][0])
            self.Entry_ido.insert('0', database_handler.recept_adatok_recept[0][2])
            self.Entry_forras.insert('0', database_handler.recept_adatok_recept[0][3])
            self.txt_elk.insert('end', database_handler.recept_adatok_recept[0][1])
            self.bevalt_check_var.set(database_handler.recept_adatok_recept[0][4])
            self.spnbox_adag.delete(0, 'end')
            self.spnbox_adag.insert(0, str(database_handler.recept_adatok_recept[0][5]))
            self.Entry_adag_me.insert('0', database_handler.recept_adatok_recept[0][6])

            if self.bevalt_check_var.get():
                self.chk_bevalt.select()


            #recept_adatok_osszetevok   pl: [('Tojás', 3.0, 'db'), ('Káposzta', 'fél', 'fej'), ('Liszt', 1.0, 'bögre')]
            for i in database_handler.recept_adatok_osszetevok:
                self.message.insert('end', '{}    {} {}'.format(i[0], i[1], i[2]))
                database_handler.osszetevok_fugg(megnevezes=i[0], mennyiseg=i[1], me=i[2])

        self.tab_order()

    def tab_order(self):
        widgets = [
            self.Entry_nev,
            self.Entry_ido,
            self.Entry_hozz_nev,
            self.Entry_menny,
            self.Entry_me,
            self.btn_hozz,
            self.spnbox_adag,
            self.Entry_adag_me,
            self.chk_bevalt,
            self.txt_elk,
            self.Entry_forras,
            self.btn_tovabb,
            self.message,
            self.btn_szerkeszt,
            self.btn_torles]

        for i in widgets:
            i.lift()

    def osszetevok_hozz_gui(self, event=''):
        megnevezes = self.Entry_hozz_nev.get().capitalize()
        mennyiseg = self.Entry_menny.get()
        me = self.Entry_me.get()

        hova = 'end'
        if self.szerk_gomb:
            hova = self.hanyadik

        if megnevezes != '':
            database_handler.osszetevok_fugg(megnevezes, mennyiseg, me, index=hova)
            self.message.insert(hova, '{}    {} {}'.format(megnevezes, mennyiseg, me))
            self.Entry_hozz_nev.delete(0, 'end')
            self.Entry_menny.delete(0, 'end'),
            self.Entry_me.delete(0, 'end')

            self.Entry_hozz_nev.focus()

        self.szerk_gomb = 0


    def torles_szerkesztes_gomb_gui(self, szerk_gomb):
        """Ha a sezrk paraméter 0 akkor a törlés funkció műküdik. Ha a paraméter 1, szerkesztés funkció működik.
        Szerkesztés esetén kitörli a mezőkban lévő adatot, visszakéri és visszaírja a handler összetevők tömbből,
        majd törli a tömbből az adatokat. törlés esetén csak a törlést hajtja végre."""

        self.szerk_gomb = szerk_gomb

        kijelolt = self.message.curselection()
        if kijelolt == ():
            pass
        else:
            self.hanyadik = self.message.index(kijelolt)
            #print('hanyadik: ', self.hanyadik)   #0-x (int)
            kijelolt_elem = kijelolt[0]
            #print('kijelolt :', ui_handler_bekeres.osszetevok_tomb[kijelolt_elem])
            if self.szerk_gomb == 1:
                self.Entry_hozz_nev.delete(0, 'end')
                self.Entry_menny.delete(0, 'end')
                self.Entry_me.delete(0, 'end')
                self.Entry_hozz_nev.insert(0, database_handler.osszetevok_tomb[kijelolt_elem][0])
                self.Entry_menny.insert(0, database_handler.osszetevok_tomb[kijelolt_elem][1])
                self.Entry_me.insert(0, database_handler.osszetevok_tomb[kijelolt_elem][2])

            database_handler.torles_fugg(kijelolt_elem)
            self.message.delete(kijelolt)

    def tovabb_gomb_gui(self, event='', szerk=0):
        """A tovább gomb gui-n belüli része.
        Meghívja az ui_handler_bekeres-ben lévő függvényt, átadja neki az adatokat(név, idő, elkészítési idő)
        elindítja az osztályhívó függvényt ui_handler-ben
        Indítja a kategória választást!"""

        nev = self.Entry_nev.get()
        ido = self.Entry_ido.get()
        elk = self.txt_elk.get('1.0', 'end-1c')
        adag = str(self.spnbox_adag.get())
        adag_me = self.Entry_adag_me.get()
        bevalt = self.bevalt_check_var.get()
        forras = self.Entry_forras.get()
        #destroy_window()
        root.destroy()
        database_handler.recept_osztaly_letre()
        database_handler.tovabb_gomb_fugg(nev, ido, elk, adag, adag_me, bevalt, forras, szerk)
        main.start_kat_valasztas(szerk=szerk)


    # jelenleg nem működik, meg kéne nyitni egy kapcsolatot az adatbázissal
    # vagy ki kell listázni az elején, egy tömbbe gyűjteni és onnan dolgozni.

    def me_kereses(self, event=''):
        """a megadott hozzávaló nevét megkeresi az adatbázisban és megpróbál mértékegységet társítani hozzá."""

        hozzavalo = self.Entry_hozz_nev.get().capitalize()
        if hozzavalo != '':     #nem üres
            bevitt_me = self.Entry_me.get()
            if bevitt_me == '':     #nem üres
                keresett_me = database_handler.mertekegyseg_kitalalas(hozzavalo=hozzavalo)
                self.Entry_me.insert('0', keresett_me)

    def forras_kitalal(self, event='', torles=0):
        """Forrás beírásakor megnézi az initben lefuttatott függvény alapján, lértehozott tömbben, hogy van-e
        egyezés, és kiegészíti."""

        global beirt    #globalként kell létrehozni, hogy ne "felejtse el"

        ncar=['BackSpace', 'Left', 'Right', 'Up', 'Down', 'Shift_L', 'Shift_R', 'Control_L', 'Control_R']

        if event.keysym not in ncar:
            beirt = self.Entry_forras.get()
            for i in database_handler.eredmeny_forras:
                if beirt in i[:len(beirt)]:
                    self.Entry_forras.insert(len(beirt), i[len(beirt):])
                    self.Entry_forras.select_range(len(beirt), 'end')
                    break

    def mozgatas(self, irany=0):
        """irány: 1 felfele, 2 lefele"""

        mozgatas_kijelolt = self.message.curselection()     #(0,) vagy (1,) index

        #print(mozgatas_kijelolt)
        if mozgatas_kijelolt != ():
            mozg_hanyadik = self.message.index(mozgatas_kijelolt)
            # print(self.mozg_hanyadik)

            szoveg = self.message.get(mozg_hanyadik)
            self.message.delete(mozg_hanyadik)

            #print('osszetevopk_tomb ', ui_handler_bekeres.osszetevok_tomb)
            mozg_elemek = database_handler.osszetevok_tomb[mozg_hanyadik]
            #print('elemek ', mozg_elemek)
            database_handler.osszetevok_tomb.pop(mozg_hanyadik)

            if irany == 1:
                self.message.insert(mozg_hanyadik-1, szoveg)
                database_handler.osszetevok_tomb.insert(mozg_hanyadik-1, mozg_elemek)
                self.message.select_set(mozg_hanyadik - 1)
            elif irany == 2:
                self.message.insert(mozg_hanyadik+1, szoveg)
                database_handler.osszetevok_tomb.insert(mozg_hanyadik+1, mozg_elemek)
                self.message.select_set(mozg_hanyadik + 1)
            else:
                self.message.insert(mozg_hanyadik, szoveg)
                database_handler.osszetevok_tomb.insert(mozg_hanyadik, mozg_elemek)
                self.message.select_set(mozg_hanyadik)
                #visszahelyezi ahonnan kiszedte, nem történik semmi.
                #le kell kezelni, hogy ne törölje ki hiba esetén sem azt amit át kell helyezni.

            #print('osszetevopk_tomb ', database_handler.osszetevok_tomb)




if __name__ == '__main__':
    vp_start_gui()
