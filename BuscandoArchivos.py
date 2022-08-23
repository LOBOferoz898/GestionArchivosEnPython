from tkinter import E

Archivos = ["pablito.txt","ApuntesComandosGIT.txt"]
val = True
while val:
    cont = 0
    for i in Archivos:
        try:
            archivo = open(i)
            print(archivo.read())     
            val = False 
        except:
            print(f"Archivo {i} no encontrado")
        
