from guardarModal import *
from modificar import *
from leer import *


class Modificar(object):
    def modifica(self, idVar, popupModificar):
        lab = Label(popupModificar, width=100, text=idVar.get())
        lab.pack(side=TOP)
        self.id_value = idVar.get()
        db = shelve.open('persona')
        form_modificar = FormularioModificar()
        try:
            self.persona_a_modificar = db[self.id_value]
            popupModificar2 = Toplevel()
            variables = form_modificar.CrearFormModificar(popupModificar2,
                                                          campos, self.id_value)
            Button(popupModificar2, text='Dar Aumento',
                   command=lambda: (self.dar_aumento())).pack()
            Button(popupModificar2, text='Guardar',
                   command=(lambda: guarda_dict(self.id_value, self.persona_a_modificar,
                                                variables, popupModificar2))).pack()
            popupModificar2.grab_set()
            popupModificar2.focus_set()
            popupModificar2.wait_window()
        except KeyError:
            texto_a_mostrar = 'No existe un id: {id_value}'.format(id_value=self.id_value)
            lab_leer = Label(popupModificar, width=100, text=texto_a_mostrar)
            lab_leer.pack(side=TOP)
        db.close()

    def modificar(self):
        popupModificar = Toplevel()
        popupModificar.geometry("400x300")
        mod = CrearFormLeer(popupModificar)
        Button(popupModificar, text='Buscar', command=(lambda:
                                                       self.modifica(mod, popupModificar))).pack()
        popupModificar.grab_set()
        popupModificar.focus_set()
        popupModificar.wait_window()

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
        Button(div2, text='Aceptar', command=lambda: percentage_win.destroy()). \
            pack(side=BOTTOM)
        lab.pack(side=TOP)
        ent.pack(side=TOP, fill=X)
        var = DoubleVar()
        ent.config(textvariable=var)
        percentage_win.grab_set()
        percentage_win.focus_set()
        percentage_win.wait_window()
        self.persona_a_modificar.darAumento(var.get())



