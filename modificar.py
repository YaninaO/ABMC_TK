from tkinter import *
from cerrar import Cerrar
import shelve
archivo = 'persona'

class FormularioModificar(object):
    float_number = 0.0
    aumento = False

    def CrearFormModificar(self, root, campos):
        formulario = Frame(root)
        div1 = Frame(formulario, width=100)
        div2 = Frame(formulario, padx=7, pady=2)
        formulario.pack(fill=X)
        div1.pack(side=LEFT)
        div2.pack(side=RIGHT, expand=YES, fill=X)
        variables = {}

        for field in campos:
            if field != 'sueldo':
                lab = Label(div1, width=10, text=field)
                ent = Entry(div2, width=30, relief=SUNKEN)
                lab.pack(side=TOP)
                ent.pack(side=TOP, fill=X)
                var = StringVar()
                ent.config(textvariable=var)
                variables[field]= var
        # Button(div2, text='Dar Aumento', command=lambda: (self.dar_aumento())).pack()
        # div2.grab_set()
        # div2.focus_set()
        # div2.wait_window()
        # variables['sueldo']= self.devolver_valor()
        # variables['darAumento'] = self.aumento
        return variables

    def dar_aumento(self):
        percentage_win = Toplevel()
        formulario = Frame(percentage_win)
        div1 = Frame(formulario, width=200)
        div2 = Frame(formulario, padx=7, pady=2)
        formulario.pack(fill=X)
        div1.pack(side=LEFT)
        div2.pack(side=RIGHT, expand=YES, fill=X)
        lab = Label(div1, width=20, text='Ingrese porcentaje: ')
        ent = Entry(div2, width=20, relief=SUNKEN)
        Button(div2, text='Aceptar', command=lambda: percentage_win.destroy()).\
            pack(side=BOTTOM)
        lab.pack(side=TOP)
        ent.pack(side=TOP, fill=X)
        var = StringVar()
        ent.config(textvariable=var)
        percentage_win.grab_set()
        percentage_win.focus_set()
        percentage_win.wait_window()
        self.float_number = ent
        self.aumento = True

    def devolver_valor(self):
        return self.float_number
