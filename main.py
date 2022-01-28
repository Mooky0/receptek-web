
#import database_handler
import ui_add
import ui_view
import ui_browser
import ui_category
import biztonsagi_mentes

def bizt_mentes():
    biztonsagi_mentes.biztonsagiMentes()

def letrehozas_gomb(event='', szerk=0):
    '''A recept létrehozás gomb függvénye.
    megnyitja a létrehozás ablakot.'''
    ui_add.vp_start_gui(szerk=szerk)

def megnyitas_gomb():
    ui_view.vp_start_gui()


def start_kat_valasztas(szerk):
    """Gui-t indít"""
    ui_category.vp_start_gui(szerk=szerk)

if __name__ == '__main__':
    ui_browser.start_gui()
    bizt_mentes()
    #database_handler.variables()
'sdf'.isnumeric()