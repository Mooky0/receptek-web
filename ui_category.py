#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Jan 02, 2020 05:44:45 PM CET  platform: Windows NT

import sys

import tkinter as tk
import tkinter.ttk as ttk

import database_handler

py3 = True


def destroy_window():
    root.destroy()

def vp_start_gui(szerk=0):
    '''Starting point when module is the main routine.'''
    global ui_category_peldany
    global root
    root = tk.Tk()
    ui_category_peldany = Ui_category_class(root, szerk=szerk)
    root.mainloop()

class Ui_category_class:
    def __init__(self, master=None, szerk=0):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font14 = "-family {Segoe UI} -size 9 -weight " \
                 "normal -slant roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        #if sys.platform == "win32":
        #    self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.map('.', background=[('selected', _compcolor), ('active', _ana2color)])

        master.geometry("539x507+447+50")

        master.minsize(500, 500)
        master.maxsize(1370, 749)
        master.resizable(1, 1)
        master.title("Címkék hozáadása")
        master.configure(background="#efefef")
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")

        self.szerk=szerk

        #Cím label

        self.lbl_cim = tk.Label(master)
        self.lbl_cim.place(relx=0.037, rely=0.02, height=41, width=384)
        self.lbl_cim.configure(activebackground="#f9f9f9", activeforeground="black", anchor='w', background="#efefef",
                              disabledforeground="#a3a3a3", font="-family {Microsoft JhengHei UI} -size 24",
                              foreground="#000000", highlightbackground="#d9d9d9", highlightcolor="black",
                              text='''Címkék hozzáadása''')

        #Tartalom keret:
        #Összetevők a napi tucatból

        self.lbl_tartalom = tk.LabelFrame(master)
        self.lbl_tartalom.place(relx=0.037, rely=0.118, relheight=0.345, relwidth=0.946)
        self.lbl_tartalom.configure(relief='groove', foreground="black", text='''Összetevők a Napi tucatból''', background="#efefef",
                                    highlightbackground="#d9d9d9", highlightcolor="black")

        self.tart_listbol = tk.Listbox(self.lbl_tartalom)
        self.tart_listbol.place(relx=0.02, rely=0.114, relheight=0.714, relwidth=0.335, bordermode='ignore')
        self.tart_listbol.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                    foreground="black", highlightbackground="#d9d9d9", highlightcolor="#d9d9d9",
                                    selectbackground="#c4c4c4", selectforeground="black", selectmode="MULTIPLE")
        self.tart_listbol.bind('<Return>', func=self.tart_hozz_gomb_gui)
        self.tart_listbol.bind('<Double-Button-1>', func=self.tart_hozz_gomb_gui)
        self.tart_listbol.bind('<Button-3>', func=self.tart_hozz_gomb_gui)


        self.tart_listbe = tk.Listbox(self.lbl_tartalom)
        self.tart_listbe.place(relx=0.647, rely=0.114, relheight=0.714, relwidth=0.335, bordermode='ignore')
        self.tart_listbe.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                   foreground="black", highlightbackground="#d9d9d9", highlightcolor="#d9d9d9",
                                   selectbackground="#c4c4c4", selectforeground="black")
        self.tart_listbe.bind('<Return>', func=self.tart_torles_gomb_gui)
        self.tart_listbe.bind('<Double-Button-1>', func=self.tart_torles_gomb_gui)
        self.tart_listbe.bind('<Button-3>', func=self.tart_torles_gomb_gui)

        self.btn_tart_hozz = tk.Button(self.lbl_tartalom)
        self.btn_tart_hozz.place(relx=0.5, rely=0.35, height=24, width=80, bordermode='ignore', anchor='center')
        self.btn_tart_hozz.configure(activebackground="#ececec", activeforeground="#000000", background="#ececec",
                                     disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                     highlightcolor="black", pady="0", text='''Hozzáadás''',
                                     command=self.tart_hozz_gomb_gui)
        self.btn_tart_hozz.bind('<Return>', func=self.tart_hozz_gomb_gui)

        self.btn_tart_tor = tk.Button(self.lbl_tartalom)
        self.btn_tart_tor.place(relx=0.5, rely=0.7, height=24, width=60, bordermode='ignore', anchor='center')
        self.btn_tart_tor.configure(activebackground="#ececec", activeforeground="#000000", background="#ececec",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", pady="0", text='''Törlés''',
                                    command=self.tart_torles_gomb_gui)
        self.btn_tart_tor.bind('<Return>', func=self.tart_torles_gomb_gui)


        #Alkalom keret
        #további címkék

        self.lbl_alkalom = tk.LabelFrame(master)
        self.lbl_alkalom.place(relx=0.037, rely=0.493, relheight=0.345, relwidth=0.946)
        self.lbl_alkalom.configure(relief='groove', foreground="black", text='''További címkék''', background="#efefef",
                                   highlightbackground="#d9d9d9", highlightcolor="black")

        self.alk_listbol = tk.Listbox(self.lbl_alkalom)
        self.alk_listbol.place(relx=0.02, rely=0.114, relheight=0.714, relwidth=0.335, bordermode='ignore')
        self.alk_listbol.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                   foreground="black", highlightbackground="#d9d9d9", highlightcolor="#d9d9d9",
                                   selectbackground="#c4c4c4", selectforeground="black")
        self.alk_listbol.bind('<Return>', func=self.alk_hozz_gomb_gui)
        self.alk_listbol.bind('<Double-Button-1>', func=self.alk_hozz_gomb_gui)
        self.alk_listbol.bind('<Button-3>', func=self.alk_hozz_gomb_gui)

        self.alk_listbe = tk.Listbox(self.lbl_alkalom)
        self.alk_listbe.place(relx=0.647, rely=0.114, relheight=0.714, relwidth=0.335, bordermode='ignore')
        self.alk_listbe.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                  foreground="black", highlightbackground="#d9d9d9", highlightcolor="#d9d9d9",
                                  selectbackground="#c4c4c4", selectforeground="black")
        self.alk_listbe.bind('<Return>', func=self.alk_torles_gomb_gui)
        self.alk_listbe.bind('<Double-Button-1>', func=self.alk_torles_gomb_gui)
        self.alk_listbe.bind('<Button-3>', func=self.alk_torles_gomb_gui)

        self.btn_alk_hozz = tk.Button(self.lbl_alkalom)
        self.btn_alk_hozz.place(relx=0.5, rely=0.35, height=24, width=80, bordermode='ignore', anchor='center')
        self.btn_alk_hozz.configure(activebackground="#ececec", activeforeground="#000000", background="#ececec",
                                    disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                    highlightcolor="black", pady="0", text='''Hozzáadás''',
                                    command=self.alk_hozz_gomb_gui)
        self.btn_alk_hozz.bind('<Return>', func=self.alk_hozz_gomb_gui)

        self.btn_alk_tor = tk.Button(self.lbl_alkalom)
        self.btn_alk_tor.place(relx=0.5, rely=0.7, height=24, width=60, bordermode='ignore', anchor='center')
        self.btn_alk_tor.configure(activebackground="#ececec", activeforeground="#000000", background="#ececec",
                                   disabledforeground="#a3a3a3", foreground="#000000", highlightbackground="#d9d9d9",
                                   highlightcolor="black", pady="0", text='''Törlés''',
                                   command=self.alk_torles_gomb_gui)
        self.btn_alk_tor.bind('<Return>', func=self.alk_torles_gomb_gui)

        self.Entry_alk = tk.Entry(self.lbl_alkalom)
        self.Entry_alk.place(relx=0.02, rely=0.857, height=20, relwidth=0.243, bordermode='ignore')
        self.Entry_alk.configure(background="white", disabledforeground="#a3a3a3", font="TkFixedFont",
                                 foreground="#000000", insertbackground="black")
        self.Entry_alk.focus()

        self.Entry_alk.bind('<Return>', func=self.alk_hozz_gomb_gui)   #valamiért egyből bezárja az ablakot.

        #Kész gomb

        self.btn_kesz = tk.Button(master)
        self.btn_kesz.place(relx=0.98, rely=0.92, height=54, width=137, anchor='e')
        self.btn_kesz.configure(activebackground="#ececec", activeforeground="#000000", background="#ececec",
                                disabledforeground="#a3a3a3", font=font14, foreground="#000000",
                                highlightbackground="#d9d9d9", highlightcolor="black", pady="0", text='''KÉSZ''',
                                command=self.kesz_gomb_gui)
        #self.Entry_alk.bind('<Return>', func=self.kesz_gomb_gui)

        self.beiras()

        database_handler.alk_tomb = []
        database_handler.tart_tomb = []

        if szerk:
            database_handler.szerk_listazas()
            for i in database_handler.alkalom_listazas_tomb:
                database_handler.alk_tomb.append(i)
                self.alk_listbe.insert('end', i)
            for i in database_handler.tartalom_listazas_tomb:
                database_handler.tart_tomb.append(i)
                self.tart_listbe.insert('end', i)

        self.tab_order()

        #fv.ek

    def beiras(self):
        """beírja a listbox-okba a lekért adat tömböket."""

        #tartalom = ui_handler_kategoria.Lekerd('tartalom')
        alkalom = database_handler.alk_tart_lekerdezes('alkalom', 'alkalom')
        napituc = database_handler.alk_tart_lekerdezes('napitucat', 'nev')

        for i in napituc:
            self.tart_listbol.insert('end', i)
        for i in alkalom:
            self.alk_listbol.insert('end', i)

    def tart_hozz_gomb_gui(self, event=''):
        """Tartalom hozzáadása"""

        def letezik(elem):
            if elem in database_handler.tart_tomb:
                return 0
            else:
                return 1

        aktiv = self.tart_listbol.get('active')
        if letezik(aktiv):
            database_handler.tart_tomb.append(aktiv)
            self.tart_listbe.insert('end', aktiv)
        else:
            print('Az elem már szerepel egyszer!')

    def alk_hozz_gomb_gui(self, event=''):
        """Alkalom hozzáadása"""
        def letezik(elem):
            if elem in database_handler.alk_tomb:
                return 1
            else:
                return 0

        bekert_alk = self.Entry_alk.get().lower()
        if bekert_alk == '':
            aktiv = self.alk_listbol.get('active')
            if not letezik(aktiv):
                database_handler.alk_tomb.append(aktiv)
                self.alk_listbe.insert('end', aktiv)
            else:
                print('Az elem már szerepel egyszer!')
        else:
            if not letezik(bekert_alk):
                database_handler.alk_tomb.append(bekert_alk)
                self.alk_listbe.insert('end', bekert_alk)
            self.Entry_alk.delete(0, 'end')

    def tart_torles_gomb_gui(self, event=''):
        try:
            aktiv = self.tart_listbe.get('active')
            self.tart_listbe.delete(self.tart_listbe.curselection())
            database_handler.tart_tomb.remove(aktiv)
        except:
            print('Nincs aktív elem')

    def alk_torles_gomb_gui(self, event=''):
        try:
            aktiv = self.alk_listbe.get('active')
            self.alk_listbe.delete(self.alk_listbe.curselection())
            database_handler.alk_tomb.remove(aktiv)
        except:
            print('Nincs aktív elem')

    def kesz_gomb_gui(self, event=''):
        """doc string"""
        database_handler.kesz_gomb_fugg()
        destroy_window()

    def tab_order(self):
        widgets = [
            self.Entry_alk,
            self.btn_alk_hozz,
            self.btn_alk_tor,
            self.btn_kesz
            ]

        for i in widgets:
            i.lift()


if __name__ == '__main__':
    vp_start_gui()
