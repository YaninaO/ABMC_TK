import shelve
from leer import *
archivo = 'persona'


def lee(idVar, popupLeer):
    lab = Label(popupLeer, width=100, text=idVar.get())
    lab.pack(side=TOP)
    t = idVar.get()
    db = shelve.open('persona')
    valorALeer = db[t]
    lab_leer = Label(popupLeer, width=100, text=valorALeer)
    lab_leer.pack(side=TOP)
    db.close()


def leer():
    popupLeer = Toplevel()
    popupLeer.geometry("400x300")
    vars_leer = CrearFormLeer(popupLeer)
    Button(popupLeer, text='Buscar',
           command=(lambda: lee(vars_leer, popupLeer))).pack()
    popupLeer.grab_set()
    popupLeer.focus_set()
    popupLeer.wait_window()