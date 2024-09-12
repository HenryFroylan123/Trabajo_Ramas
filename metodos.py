import tkinter
import pyodbc
from tkinter import *
import tkinter as tk

direccion_servidor = "DESKTOP-T1305OM\SQLEXPRESS"
nombre_bd = "tarea"
nombre_usuario = "sa"
password = "123"

try:
    conexion = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=' +
                              direccion_servidor + ';DATABASE=' + nombre_bd + ';UID=' + nombre_usuario + ';PWD=' + password)
    print("Ok! Conexion exitosa")
except Exception as e:
    print("Ocurrió un error al conectarse a SQL Server", e)



root = Tk()
root.title("Crud Python")




nombre = StringVar()
cantidad = IntVar()
miframe = Frame(root, width=500, height=400)

miframe.pack()
milabel = Label(miframe, text="Bienvenido al crud python").place(x=0, y=0)
milabel = Label(miframe, text="Cantidad del producto:").place(x=100, y=100)
milabel = Label(miframe, text="Ingrece los siguientes datos:").place(x=200, y=50)
milabel = Label(miframe, text="Nombre del producto:").place(x=100, y=200)

cuadro1 = Entry(miframe, textvariable=nombre).place(x=300, y=200)

cuadro2 = Entry(miframe, textvariable=cantidad).place(x=300, y=100)


def codigoBoton():
    print(str(nombre.get()))
    print(str(cantidad.get()))
    try:
        with conexion.cursor() as cursor:
            consulta = "INSERT INTO tiendas(nombre, piezas) VALUES " \
                       "(?, ?);"
            # Podemos llamar muchas veces a .execute con datos distintos

            cursor.execute(consulta, (nombre.get(), cantidad.get()))
    except Exception as e:
        print("Ocurrió un error al insertar: ", e)
    finally:
        conexion.close()

botonEnvio = Button(root, text="Capturar", command=codigoBoton)
botonEnvio.pack()

root.mainloop()

# ______________________________abajo esta el codigo crud____________________________#

