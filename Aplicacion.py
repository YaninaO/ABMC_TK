from tkinter import *
from guardarModal import *
from leerModal import *
from borrarModal import *
from modificarModal import *
from cerrar import Cerrar

class MiApp:

    def __init__(self, parent=None, **configs):
        # ##################################################################
        # Ventana principal
        # ##################################################################
        self.myParent = parent
        self.myParent.geometry("300x300")
        # ##################################################################
        # Agrego contenedor
        # ##################################################################
        self.Contenedor = Frame(self.myParent, bg="light grey")
        self.Contenedor.pack(expand=YES, fill=BOTH)

        fg = "light green",
        bg = "dark green",
        font = "Helvetica 18 bold"

        Label(self.Contenedor, text='ABMC', font=font).pack(side=TOP)
        # ##################################################################
        # Agrego Secciones Principales
        # ##################################################################
        #####  CERRAR #####
        self.seccion_cerrar = Frame(self.Contenedor, bg="#FF7F50", height=22,
        borderwidth=2, relief=RAISED)
        self.seccion_cerrar.pack(side=TOP, expand=NO, fill=X,
        padx=7)
        self.cerrar = Frame(self.seccion_cerrar, bg="#222", height=22)
        self.cerrar.pack(side=TOP, expand=NO, fill=X)

        #####  SECCION CONTROLES #####
        self.seccion_controles = Frame(self.Contenedor, bg="red",
        borderwidth=2, relief=RAISED)
        self.seccion_controles.pack(side=TOP, expand=NO, fill=BOTH,
        padx=7, pady=7)
        titulo_controles = "Controles"
        Label(self.seccion_controles, text=titulo_controles,
        bg="#222",fg="OrangeRed",
        justify=LEFT).pack(side=TOP, expand=NO, fill=X, anchor=W)
        self.controles = Frame(self.seccion_controles, bg="#222")
        self.controles.pack(side=TOP, expand=NO, fill=X)

        mod_class = Modificar()
        ancho_boton = 10
        boton1 = Button(self.seccion_controles, text='Guardar', command=guardar)
        boton1["width"] = ancho_boton
        boton2 = Button(self.seccion_controles, text='Leer', command=leer)
        boton2["width"] = ancho_boton
        boton3 = Button(self.seccion_controles, text='Borrar', command=borrar)
        boton3["width"] = ancho_boton
        boton4 = Button(self.seccion_controles, text='Modificar',
                        command=mod_class.modificar)
        boton4["width"] = ancho_boton
        boton1.pack()
        boton2.pack()
        boton3.pack()
        boton4.pack()
        Cerrar(self.seccion_cerrar)

if __name__ == '__main__':
    root = Tk()
    MiApp(root)
    root.iconbitmap(bitmap="@icono.xbm")
    root.mainloop()

