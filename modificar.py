from tkinter import *


class FormularioModificar(object):
    def CrearFormModificar(self, root, campos, id_value):
        formulario = Frame(root)
        div1 = Frame(formulario, width=100)
        div2 = Frame(formulario, padx=7, pady=2)
        formulario.pack(fill=X)
        div1.pack(side=LEFT)
        div2.pack(side=RIGHT, expand=YES, fill=X)
        variables = {}
        lab2 = Label(div1, width=10, text='Id')
        lab2.pack(side=TOP)
        lab3 = Label(div2, width=30, text=id_value)
        lab3.pack(side=TOP)
        for field in campos:
            if field != 'sueldo' and field != 'id':
                lab = Label(div1, width=10, text=field)
                ent = Entry(div2, width=30, relief=SUNKEN)
                lab.pack(side=TOP)
                ent.pack(side=TOP, fill=X)
                var = StringVar()
                ent.config(textvariable=var)
                variables[field]= var
        return variables
