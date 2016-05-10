import shelve
from leer import *
archivo = 'persona'


def lee(idVar, popupLeer):
    id_value = idVar.get()
    db = shelve.open('persona')
    try:
        valorALeer = db[id_value]
        lab_leer = Label(popupLeer, width=100,
                         text='Informacion del Id: {} \n {}'.format(id_value, valorALeer))
        lab_leer.pack(side=TOP)
    except KeyError:
        texto_a_mostrar = 'No existe un id: {id_value}'.format(id_value=id_value)
        lab_leer = Label(popupLeer, width=100, text=texto_a_mostrar)
        lab_leer.pack(side=TOP)
    db.close()


def leer():
    popupLeer = Toplevel()
    popupLeer.geometry("300x300")
    font = "Helvetica 12 bold"
    Label(popupLeer, text='Ingrese Id para leer', font=font).pack(side=TOP)
    vars_leer = CrearFormLeer(popupLeer)
    Button(popupLeer, text='Buscar',
           command=(lambda: lee(vars_leer, popupLeer))).pack()
    popupLeer.grab_set()
    popupLeer.focus_set()
    popupLeer.wait_window()