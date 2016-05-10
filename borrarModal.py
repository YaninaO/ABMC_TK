import shelve
from borrar import *
archivo = 'persona'


def borra(idVar, popupLeer):
    lab = Label(popupLeer, width=100,
                text='Id borrado: {}'.format(idVar.get()))
    lab.pack(side=TOP)
    id_value = idVar.get()
    db = shelve.open('persona')
    try:
        del db[id_value]
    except:
        texto_a_mostrar = 'No existe un id: {id_value}'.format(id_value=id_value)
        lab_leer = Label(popupLeer, width=100, text=texto_a_mostrar)
        lab_leer.pack(side=TOP)
    db.close()


def borrar():
    popupBorrar = Toplevel()
    popupBorrar.geometry("200x200")
    font = "Helvetica 12 bold"
    Label(popupBorrar, text='Ingrese Id para borrar', font=font).pack(side=TOP)
    borrar = CrearFormBorrar(popupBorrar)
    Button(popupBorrar, text='Borrar',
           command=(lambda: borra(borrar, popupBorrar))).pack()
    popupBorrar.grab_set()
    popupBorrar.focus_set()
    popupBorrar.wait_window()