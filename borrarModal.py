import shelve
from borrar import *
archivo = 'persona'


def borra(idVar, popupLeer):
    lab = Label(popupLeer, width=100, text=idVar.get())
    lab.pack(side=TOP)
    t = idVar.get()
    db = shelve.open('persona')
    del db[t]
    db.close()


def borrar():
    popupBorrar = Toplevel()
    popupBorrar.geometry("400x300")
    borrar = CrearFormBorrar(popupBorrar)
    Button(popupBorrar, text='Borrar',
           command=(lambda: borra(borrar, popupBorrar))).pack()
    popupBorrar.grab_set()
    popupBorrar.focus_set()
    popupBorrar.wait_window()