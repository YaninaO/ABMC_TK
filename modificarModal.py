from tkinter import *
import shelve
from modificar import *
from guardar import *
from leer import *
from guardarModal import *
from PersonaP.PersonaM import Persona
archivo = 'persona'


def modifica(idVar, popupModificar):
    lab = Label(popupModificar, width=100, text=idVar.get())
    lab.pack(side=TOP)
    t = idVar.get()
    db = shelve.open('persona')
    # valorABorrar = db[t]
    popupModificar2 = Toplevel()
    print campos
    variables = CrearFormModificar(popupModificar2, campos)
    persona_a_modificar = db[t]
    lista = []
    for variable in variables:
        lista.append(variable.get())
    persona_a_modificar.nombre = lista[1]
    persona_a_modificar.edad = lista[2]
    persona_a_modificar.sueldo = lista[3]
    persona_a_modificar.trabajo = lista[4]
    valor_id = lista[0]
    db = shelve.open('persona')
    #guardoValor = Persona(lista[1], lista[2], lista[3], lista[4])
    guardarValor = persona_a_modificar
    db[lista[0]] = guardarValor
    db.close()

    Button(popupModificar2, text='guardar',
           command=(lambda: guarda(variables, popupModificar2))).pack()
    popupModificar2.grab_set()
    popupModificar2.focus_set()
    popupModificar2.wait_window()
    db.close()

def modificar():
    popupModificar = Toplevel()
    popupModificar.geometry("400x300")
    mod = CrearFormLeer(popupModificar)
    Button(popupModificar, text='Buscar', command=(lambda:
                                            modifica(mod, popupModificar))).pack()
    popupModificar.grab_set()
    popupModificar.focus_set()
    popupModificar.wait_window()


