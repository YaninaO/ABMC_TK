from tkinter import *
import shelve
from guardar import *
from PersonaP.PersonaM import Persona
archivo = 'persona'

def guarda_dict(id, persona_a_modificar,variables, popupGuardar):
    popupGuardar.destroy()
    persona_a_modificar.nombre = variables['nombre'].get()  # lista[1]
    persona_a_modificar.edad = variables['edad'].get()
    persona_a_modificar.trabajo = variables['trabajo'].get()
    db = shelve.open('persona')
    db[id] = persona_a_modificar
    db.close()


def guarda(variables, popupGuardar):
    popupGuardar.destroy()
    lista = []
    for variable in variables:
        lista.append(variable.get())
    db = shelve.open('persona')
    guardoValor = Persona(lista[1], lista[2], lista[3], lista[4])
    db[lista[0]] = guardoValor
    db.close()


def guardar():
    popupGuardar = Toplevel()
    vars_guardar = CrearFormGuardar(popupGuardar, campos)
    Button(popupGuardar, text='Guardar',
           command=(lambda: guarda(vars_guardar, popupGuardar))).pack()
    popupGuardar.grab_set()
    popupGuardar.focus_set()
    popupGuardar.wait_window()
