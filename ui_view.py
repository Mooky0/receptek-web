#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Nov 11, 2020 01:40:15 PM CET  platform: Windows NT

import sys

import tkinter as tk
import tkinter.ttk as ttk

import database_handler
import main

def vp_start_gui(szerk=0):
    '''Starting point when module is the main routine.'''
    global ui_view_peldany
    global root
    root = tk.Tk()
    ui_category_peldany = Ui_view_class(root)
    root.mainloop()


class Ui_view_class:
    def __init__(self, master=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        # _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _bgcolor = '#39dd4e'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 14 -weight bold -slant " \
                 "roman -underline 1 -overstrike 0"
        font11 = "-family {Segoe UI} -size 12 -weight normal -slant " \
                 "roman -underline 0 -overstrike 0"
        font12 = "-family {Segoe UI} -size 12 -weight bold -slant " \
                 "roman -underline 0 -overstrike 0"
        font13 = "-family {Segoe UI} -size 11 -weight normal -slant " \
                 "roman -underline 0 -overstrike 0"

        master.geometry("600x528+{}+{}".format(int((master.winfo_screenwidth()-600)/2), int((master.winfo_screenheight()-528)/2)))
        # master.geometry("600x528+648+212")


        master.minsize(120, 1)
        #master.maxsize(1924, 1061)
        master.resizable(1, 1)
        master.title("Recept megtekintés")
        master.configure(background="#d9d9d9")
        # master.configure(background="#39dd4e")

        self.lbl_recept_cim = tk.Label(master)
        self.lbl_recept_cim.place(relx=0.017, rely=0.019, height=31, width=584)
        self.lbl_recept_cim.configure(background="#d9d9d9", disabledforeground="#a3a3a3", font=font10,
                                      foreground="#000000")

        self.lbl_hozzavalok = tk.Label(master)
        self.lbl_hozzavalok.place(relx=0.000, rely=0.076, height=31, width=114)
        self.lbl_hozzavalok.configure(background="#d9d9d9", disabledforeground="#a3a3a3", font=font12,
                                      foreground="#000000", text='''Hozzávalók:''')

        self.lbl_napitucat = tk.Label(master)
        self.lbl_napitucat.place(relx=0.495, rely=0.076, height=31, width=114)
        self.lbl_napitucat.configure(background="#d9d9d9", disabledforeground="#a3a3a3", font=font12,
                                     foreground="#000000", text='''Napi tucat:''')

        self.scrollbar_treeview_hozzavalok = tk.Scrollbar(master)
        self.scrollbar_treeview_hozzavalok.place(relx=0.017 + 0.449, rely=0.133, relheight=0.33)
        self.treeview_hozzavalok = ttk.Treeview(master, yscrollcommand=self.scrollbar_treeview_hozzavalok.set)
        self.treeview_hozzavalok.place(relx=0.017, rely=0.133, relheight=0.33, relwidth=0.449)
        self.treeview_hozzavalok['columns'] = ('mennyiseg', 'mertekegyseg')
        self.treeview_hozzavalok.column('#0', width=135)
        self.treeview_hozzavalok.column('mennyiseg', width=30)  # 70
        self.treeview_hozzavalok.column('mertekegyseg', width=7)  # 70
        self.treeview_hozzavalok.heading('#0', text='Név')
        self.treeview_hozzavalok.heading('mennyiseg', text='Mennyiség')
        self.treeview_hozzavalok.heading('mertekegyseg', text='Me.')
        self.scrollbar_treeview_hozzavalok.config(command=self.treeview_hozzavalok.yview)

        self.scrollbar_list_napitucat = tk.Scrollbar(master)
        self.scrollbar_list_napitucat.place(relx=0.517 + 0.440, rely=0.133, relheight=0.195)
        self.list_napitucat = tk.Listbox(master, yscrollcommand=self.scrollbar_list_napitucat.set)
        self.list_napitucat.place(relx=0.517, rely=0.133, relheight=0.195, relwidth=0.440)
        self.list_napitucat.configure(background="white", disabledforeground="#a3a3a3",
                                      font="-family {Segoe UI} -size 10", foreground="#000000",
                                      highlightbackground="#d9d9d9", highlightcolor="black", selectbackground="#c4c4c4",
                                      selectforeground="black", takefocus="0", selectmode="MULTIPLE")
        self.scrollbar_list_napitucat.config(command=self.list_napitucat.yview)

        self.lbl_adag = tk.Label(master)
        self.lbl_adag.place(relx=0.504, rely=0.335, height=21, width=64)
        self.lbl_adag.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9",
                                disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 12 -weight bold",
                                foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                justify='left', text='''Adag:''')

        adaglist = ['-', '0.5']
        for i in range(1, 101): adaglist.append(str(i))

        self.spnbox_adag = tk.Spinbox(master)
        self.spnbox_adag.place(relx=0.615, rely=0.335, height=21, width=39)
        self.spnbox_adag.configure(activebackground="#f9f9f9", background="#ffffff",
                                   font="-family {Segoe UI} -size 9",
                                   foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                   values=tuple(adaglist), command=self.adagmodositas)
        self.spnbox_adag.bind('<KeyRelease>', self.adagmodositas)

        self.lbl_adag_me = tk.Label(master)
        self.lbl_adag_me.place(relx=0.685, rely=0.335, height=21, width=74)
        self.lbl_adag_me.configure(activebackground="#f9f9f9", activeforeground="black",
                                   background="#d9d9d9", disabledforeground="#a3a3a3",
                                   font="-family {Segoe UI} -size 10", justify='left', anchor="w",
                                   foreground="#000000", highlightbackground="#d9d9d9",
                                   highlightcolor="black")

        self.lbl_forras = tk.Label(master)
        self.lbl_forras.place(relx=0.508, rely=0.375, height=21, width=64)
        self.lbl_forras.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9",
                                  disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 12 -weight bold",
                                  foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                  justify='left', text='''Forrás:''')

        self.entry_forras = tk.Entry(master)
        self.entry_forras.place(relx=0.517, rely=0.425, height=20, relwidth=0.466)
        self.entry_forras.configure(background="white", disabledbackground="white", disabledforeground="black",
                                    font="-family {Segoe UI} -size 10",
                                    foreground="#000000", insertbackground="black")

        self.lbl_elkeszites = tk.Label(master)
        self.lbl_elkeszites.place(relx=0.0, rely=0.491, height=31, width=104)
        self.lbl_elkeszites.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9",
                                      disabledforeground="#a3a3a3",
                                      font="-family {Segoe UI} -size 12 -weight bold", foreground="#000000",
                                      highlightbackground="#d9d9d9", highlightcolor="black", text='''Elkészítés:''')

        self.lbl_elkeszitesi_ido = tk.Label(master)
        self.lbl_elkeszitesi_ido.place(relx=0.633, rely=0.491, height=31, width=144)
        self.lbl_elkeszitesi_ido.configure(activebackground="#f9f9f9", activeforeground="black", background="#d9d9d9",
                                           disabledforeground="#a3a3a3",
                                           font="-family {Segoe UI} -size 12 -weight bold",
                                           foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                           text='''Elkészítési idő:''')

        self.lbl_elkeszitesi_ido_perc = tk.Label(master)
        self.lbl_elkeszitesi_ido_perc.place(relx=0.85, rely=0.491, height=31, width=74)
        self.lbl_elkeszitesi_ido_perc.configure(activebackground="#f9f9f9", activeforeground="black",
                                                background="#d9d9d9", disabledforeground="#a3a3a3",
                                                font="-family {Segoe UI} -size 12",
                                                foreground="#000000", highlightbackground="#d9d9d9",
                                                highlightcolor="black")

        self.scrollbar_txt_elkeszites = tk.Scrollbar(master)
        self.scrollbar_txt_elkeszites.place(relx=0.017+0.940, rely=0.549, relheight=0.33)
        self.txt_elkeszites = tk.Text(master, yscrollcommand=self.scrollbar_txt_elkeszites.set)
        self.txt_elkeszites.place(relx=0.017, rely=0.549, relheight=0.33, relwidth=0.940)
        self.txt_elkeszites.configure(background="white", font=font13, foreground="black",
                                      highlightbackground="#c3c3c3", highlightcolor="black", insertbackground="black",
                                      selectbackground="#c4c4c4", selectforeground="black", wrap="word")
        self.scrollbar_txt_elkeszites.config(command=self.txt_elkeszites.yview)

        self.btn_bezar = tk.Button(master)
        self.btn_bezar.place(relx=0.017, rely=0.909, height=34, width=167)
        self.btn_bezar.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                                 disabledforeground="#a3a3a3", font=font11, foreground="#000000",
                                 highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''Bezár''',
                                 command=self.ablak_bezaras)

        self.btn_torles = tk.Button(master)
        self.btn_torles.place(relx=0.362, rely=0.909, height=34, width=167)
        self.btn_torles.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                                  disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 12",
                                  foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black", pady="0",
                                  text='''Törlés''', command=self.recept_torles_ui)

        self.btn_szerkeszt = tk.Button(master)
        self.btn_szerkeszt.place(relx=0.7, rely=0.909, height=34, width=167)
        self.btn_szerkeszt.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                                     disabledforeground="#a3a3a3", font="-family {Segoe UI} -size 12",
                                     foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                     pady="0", text='''Szerkesztés''',
                                     command=lambda: main.letrehozas_gomb(szerk=1))

        self.chk_bevalt = tk.Checkbutton(master)
        self.chk_bevalt.place(relx=0.317, rely=0.491, relheight=0.047, relwidth=0.218)
        self.chk_bevalt.configure(activebackground="#ececec", activeforeground="#000000", background="#d9d9d9",
                                  disabledforeground="#000000", font="-family {Segoe UI} -size 12",
                                  foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                                  justify='left', takefocus="0", text='''Bevált recept''', state="disabled")

        self.kilistazas()

    def kilistazas(self):
        database_handler.recept_megnyitas()
        # view_handler.recept_adatok_recept  [('Példa recept', 'leírás', 20, forras, 0)]
        self.lbl_recept_cim.configure(text='{}'.format(database_handler.recept_adatok_recept[0][0]))
        self.lbl_elkeszitesi_ido_perc.configure(text='{} perc'.format(database_handler.recept_adatok_recept[0][2]))
        self.lbl_adag_me.configure(text='{}'.format(database_handler.recept_adatok_recept[0][6]))
        self.txt_elkeszites.insert('end', '{}'.format(database_handler.recept_adatok_recept[0][1]))
        self.txt_elkeszites.configure(state='disabled')
        if database_handler.recept_adatok_recept[0][4]:
            self.chk_bevalt.select()
        self.tree_listazas(database_handler.recept_adatok_osszetevok)
        if database_handler.recept_adatok_tartalom != []:
            for i in database_handler.recept_adatok_tartalom:
                self.list_napitucat.insert('end', i[0])

        self.spnbox_adag.delete(0, 'end')
        self.spnbox_adag.insert(0, database_handler.recept_adatok_recept[0][5])

        self.entry_forras.insert('0', database_handler.recept_adatok_recept[0][3])
        self.entry_forras.configure(state='disabled')

    def tree_listazas(self, adat_tomb, szorzo=1):
        """Kilistázza az elemeket. előtte törli az összes már megjelenített elemet.
        ha a szűrés paraméter 1 akkor megszűri, hogy mit listázzon ki."""
        # adat_tomb pl: [('Tojás', 3.0, 'db'), ('Káposzta', 'fél', 'fej'), ('Liszt', 1.0, 'bögre')]

        # ez a rész kéri le a 'gyerek' sorokat, majd ezen futtatja végig a tömböt és törli az összes elemet.
        for i in self.treeview_hozzavalok.get_children():
            self.treeview_hozzavalok.delete(i)

        for i in adat_tomb:

            if i[1] == '':
                self.treeview_hozzavalok.insert("", 'end', text=i[0], values=('', i[2]))
            elif type(i[1]) is int or type(i[1]) is float:
                self.treeview_hozzavalok.insert("", 'end', text=i[0], values=(round(i[1] * szorzo, 1), i[2]))
            elif type(i[1]) is str:
                # print('string')
                beirando = i[1].replace(',', '.')
                try:
                    # print('try')
                    beirando = float(beirando)
                    self.treeview_hozzavalok.insert("", 'end', text=i[0], values=(round(beirando * szorzo, 1), i[2]))
                    # print('try end')
                except:
                    # print('except')
                    if szorzo == 1:
                        self.treeview_hozzavalok.insert("", 'end', text=i[0], values=(beirando, i[2]))
                    else:
                        self.treeview_hozzavalok.insert("", 'end', text=i[0],
                                                        values=('{}x {}'.format(szorzo, beirando), i[2]))
                    # print('except end')
            else:
                # print('else')
                self.treeview_hozzavalok.insert("", 'end', text=i[0], values=('{}x {}'.format(szorzo, i[1]), i[2]))

    def adagmodositas(self, event=''):

        def szam(a):
            try:
                float(a)
                return 1
            except:
                return 0

        eredeti_adag = database_handler.recept_adatok_recept[0][5]
        if eredeti_adag != '-':
            eredeti_adag = float(eredeti_adag)
            jelenlegi_adag = self.spnbox_adag.get()
            if (jelenlegi_adag != ('-') and jelenlegi_adag != '' and szam(jelenlegi_adag)):
                jelenlegi_adag = float(jelenlegi_adag)
                self.tree_listazas(adat_tomb=database_handler.recept_adatok_osszetevok, szorzo=(jelenlegi_adag / eredeti_adag))
            elif jelenlegi_adag == '-':
                self.tree_listazas(adat_tomb=database_handler.recept_adatok_osszetevok,
                                   szorzo=1)
        else:
            eredeti_adag = 1
            jelenlegi_adag = self.spnbox_adag.get()

            if (jelenlegi_adag != ('-') and jelenlegi_adag != '' and szam(jelenlegi_adag)):
                jelenlegi_adag = float(jelenlegi_adag)
                self.tree_listazas(adat_tomb=database_handler.recept_adatok_osszetevok, szorzo=(jelenlegi_adag / eredeti_adag))
            elif jelenlegi_adag == '-':
                self.tree_listazas(adat_tomb=database_handler.recept_adatok_osszetevok,
                                   szorzo=(1))

    def recept_torles_ui(self):
        torlod = tk.messagebox.askquestion('Recept törlése', 'Biztosan törlöd ezt a receptet?',
                                           icon='warning')
        if torlod == 'yes':
            database_handler.recept_torles()
        else:
            pass

    def ablak_bezaras(self):
        root.destroy()


if __name__ == '__main__':
    vp_start_gui()
