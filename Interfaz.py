import tkinter as tk

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

from Conexion import *
from Clientes import *


class FormularioUsuarios:
    global base
    base=None

    global textBoxId
    textBoxId=None

    global textBoxNombres
    textBoxId=None

    global textBoxApellidos
    textBoxId=None

    global textBoxEdad
    textBoxId=None

    global combo
    combo=None

    global groupBox
    groupBox=None

    global tree
    tree=None

def Formulario():
        global textBoxId
        global textBoxNombres
        global textBoxApellidos
        global textBoxEdad
        global combo
        global base
        global groupBox
        global tree

        try:
              
            base= Tk()
            base.geometry("1450x300")
            base.title("CRUD Python + AQLite")
        
            groupBox = LabelFrame(base,text="Datos del Usuario",padx=5,pady=5)
            groupBox.grid(row=0,column=0,padx=10,pady=10)

            LabelId = Label(groupBox,text="Id:",width=13,font=("arial",12)).grid(row=0,column=0)
            textBoxId = Entry(groupBox)
            textBoxId.grid(row=0,column=1)
        
            LabelNombres = Label(groupBox,text="Nombres:",width=13,font=("arial",12)).grid(row=1,column=0)
            textBoxNombres= Entry(groupBox)
            textBoxNombres.grid(row=1,column=1)

            LabelApellidos = Label(groupBox,text="Apellidos:",width=13,font=("arial",12)).grid(row=2,column=0)
            textBoxApellidos = Entry(groupBox)
            textBoxApellidos.grid(row=2,column=1)

            LabelSexo = Label(groupBox,text="Sexo:",width=13,font=("arial",12)).grid(row=3,column=0)
            seleccionSexo = tk.StringVar()
            combo = ttk.Combobox(groupBox,values=["Masculino","Femenino"],textvariable=seleccionSexo)
            combo.grid(row=3,column=1)
            seleccionSexo.set("Masculino")

            LabelEdad = Label(groupBox,text="Edad:",width=13,font=("arial",12)).grid(row=4,column=0)
            textBoxEdad = Entry(groupBox)
            textBoxEdad.grid(row=4,column=1)

            Button(groupBox,text="Guardar",width=10,command=guardarRegistros).grid(row=5,column=0)
            Button(groupBox,text="Modificar",width=10,command=ModificarRegistros).grid(row=5,column=1)
            Button(groupBox,text="Eliminar",width=10,command=EliminarRegistros).grid(row=5,column=2)

            groupBox = LabelFrame(base,text="Lista de Usuarios",padx=5, pady=5)
            groupBox.grid(row=0,column=1,padx=5,pady=5)

            tree = ttk.Treeview(groupBox,columns=("Id","Nombres","Apellidos","Sexo","edad"),show="headings",height=5,)
            tree.column('# 1',anchor=CENTER)
            tree.heading('# 1',text="Id")
            tree.column('# 2',anchor=CENTER)
            tree.heading('# 2',text="Nombres")
            tree.column('# 3',anchor=CENTER)
            tree.heading('# 3',text="Apellidos")
            tree.column('# 4',anchor=CENTER)
            tree.heading('# 4',text="Sexo")
            tree.column('# 5',anchor=CENTER)
            tree.heading('# 5',text="Edad")

            vsb= Scrollbar(groupBox,orient="vertical",command=tree.yview)
  
            tree.configure(yscrollcommand=vsb.set)

            tree.pack(side=LEFT,fill=BOTH,expand=True)
            vsb.pack(side=RIGHT,fill=Y)

    
            #ACA LLENAMOS LA TABLA DE BASE DE DATOS

            for row in CClientes.mostrarClientes():
                 tree.insert("","end", values=row)

            tree.bind("<<TreeviewSelect>>",seleccionarRegistro)



            base.mainloop()

        except ValueError as error:
             print("Error de interfaz"+ error)

def guardarRegistros():
     
     
        global textBoxNombres
        global textBoxApellidos
        global textBoxEdad
        global combo
        global groupBox

        try:
              
              if textBoxNombres is None or textBoxApellidos is None or textBoxEdad is None or combo is None:
                    print("Los Widgets no inicializaron")
                    return
              nombres=textBoxNombres.get()
              apellidos=textBoxApellidos.get()
              sexo=combo.get()
              edad=textBoxEdad.get()

              CClientes.ingresarUsuario( nombres, apellidos, sexo,edad)
              messagebox.showinfo("Informacion","Los datos han sido guardados")

              actualizarTreeView()

              textBoxNombres.delete(0,END)
              textBoxApellidos.delete(0,END)
              textBoxEdad.delete(0,END)


        except ValueError as error:
             print("Error al mostrar registros{error}")

def actualizarTreeView():
      
      global tree 

      try:
            tree.delete(*tree.get_children())

            datos = CClientes.mostrarClientes()

            for row in CClientes.mostrarClientes():
                 tree.insert("","end", values=row)

      except ValueError as error:
             print("Error al mostrar registros{error}")


def seleccionarRegistro(event):
      
      try:
            itemSeleccionado = tree.focus()

            if itemSeleccionado:
                  values = tree.item(itemSeleccionado)['values']

                  textBoxId.delete(0,END)
                  textBoxId.insert(0,values[0])
                  
                  textBoxNombres.delete(0,END)
                  textBoxNombres.insert(0,values[1])

                  textBoxApellidos.delete(0,END)
                  textBoxApellidos.insert(0,values[2])

                  combo.set(values=[3])

                  textBoxEdad.delete(0,END)
                  textBoxEdad.insert(0,values[4])

      except ValueError as error:
             print("Error al mostrar registros{error}")


def ModificarRegistros():
     
        global textBoxId
        global textBoxNombres
        global textBoxApellidos
        global textBoxEdad
        global combo
        global groupBox

        try:
              
              if textBoxId is None or textBoxNombres is None or textBoxApellidos is None or textBoxEdad is None or combo is None:
                    print("Los Widgets no inicializaron")
                    return
              
              idUsuario=textBoxId.get()
              nombres=textBoxNombres.get()
              apellidos=textBoxApellidos.get()
              sexo=combo.get()
              edad=textBoxEdad.get()

              CClientes.modificarUsuario(idUsuario, nombres, apellidos, sexo,edad)
              messagebox.showinfo("Informacion","Los datos han sido actualizados")

              actualizarTreeView()


              textBoxId.delete(0,END)
              textBoxNombres.delete(0,END)
              textBoxApellidos.delete(0,END)
              textBoxEdad.delete(0,END)
              combo.set("Masculino")


        except ValueError as error:
             print("Error al mostrar registros{error}")


def EliminarRegistros():
     
        global textBoxId
        global textBoxNombres
        global textBoxApellidos
        global textBoxEdad
        global combo
        global groupBox




        try:
              
              if textBoxId is None:
                    print("Los Widgets no inicializaron")
                    return
              
              idUsuario=textBoxId.get()
              

              CClientes.eliminarUsuario(idUsuario)
              messagebox.showinfo("Informacion","Los datos han sido Eliminados")

              actualizarTreeView()


              textBoxId.delete(0,END)
              textBoxNombres.delete(0,END)
              textBoxApellidos.delete(0,END)
              textBoxEdad.delete(0,END)
              combo.set("Masculino")


        except ValueError as error:
             print("Error al mostrar registros{error}")


Formulario()