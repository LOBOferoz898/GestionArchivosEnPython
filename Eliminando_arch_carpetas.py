from genericpath import exists
import os

#ELIMINANDO UN ARCHIVO
if os.path.exists("NuevoARCHIVO.py"):
    os.remove("NuevoARCHIVO.py")
else:
    print("EL ARCHIVO NO EXISTE")


#ELIMINANDO UNA CARPETA
if os.path.exists("micarpete"):
    os.rmdir("micarpete")
else:
    print("esta carpeta no existe")