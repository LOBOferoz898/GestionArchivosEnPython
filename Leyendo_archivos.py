ApuntesComand = open("ApuntesComandosGIT.txt") #abrimos nuestro archivo que vamos a manimular en nuestro programa


print(ApuntesComand.read()) #leemos el archivo completo con read() y lo mostramos por consola

for linea in range(0,3):
    print(ApuntesComand.readline()) #leemos linea por linea 

ApuntesComand.close 