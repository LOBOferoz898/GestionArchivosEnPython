#   escribir una funcion que reciba 
#   nombre y apellido y los vaya agregando a un archivo
import os

def Agregar(nombre,apellido):
    val = True
    while val:
        if os.path.exists("ArchivoNombreApell.txt"):
            archivo = open("ArchivoNombreAppell.txt","a")
            archivo.write(f"\nnombre: {nombre}     apellido: {apellido}")
            print("Nombre y Apellido agregado con exito")
            val = False
        else:
            archivo = open("ArchivoNombreApell.txt", "x")
            print("ArchivoNombreApell.txt CREADO CON EXITO")

nombre = input("Ingrese nombre: ")
apellido = input("ingrese apellido: ")

Agregar(nombre,apellido)

