from tkinter import *
from cerrar import Cerrar


def CrearFormBorrar(root):
    formulario = Frame(root)
    div0 = Frame(formulario)
    formulario.pack(fill=X)
    div0.pack(side=TOP, expand=YES, fill=X)
    id_leer = Entry(div0, width=10)
    id_leer.pack(side=TOP)
    idVar = StringVar()
    id_leer.config(textvariable=idVar)
    idVar.set("---")
    return idVar


if __name__ == '__main__':
    root = Tk()
    vars_leer = CrearFormBorrar(root)
    Cerrar(root).pack(side=RIGHT)
    root.bind('<Return>', (lambda event: borrar(vars_leer)))
    root.mainloop()