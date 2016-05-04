from tkinter import *
import shelve
from guardar import *
from PersonaP.PersonaM import Persona
archivo = 'persona'

def guarda_dict(variables, popupGuardar):
    print variables
    print (variables['id'])
    popupGuardar.destroy()
    guardoValor = Persona(variables['nombre'], variables['edad'],
                          variables['sueldo'],variables['trabajo'])
    db = shelve.open('persona')
    db[variables['id'].get()] = guardoValor
    db.close()


def guarda(variables, popupGuardar):
    popupGuardar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())
    valor_id = lista[0]
    db = shelve.open('persona')
    guardoValor = Persona(lista[1], lista[2], lista[3], lista[4])
    db[lista[0]] = guardoValor
    db.close()


def guardar():
    popupGuardar = Toplevel()
    vars_guardar = CrearFormGuardar(popupGuardar, campos)
    Button(popupGuardar, text='Guardar', command=(lambda: guarda(vars_guardar, popupGuardar))).pack()
    popupGuardar.grab_set()
    popupGuardar.focus_set()
    popupGuardar.wait_window()
