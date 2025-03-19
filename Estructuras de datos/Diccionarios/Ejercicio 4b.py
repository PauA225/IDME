"""Programa que lea por teclado una frase y nos devuelva un diccionario con 
la cantidad de apariciones de cada carácter en la cadena."""

# Importacion de librerías:

from os import system

# Declaracion de Variables.

letras = {} # Contendra las letras (Clave) y el numero de veces que aparece (Valor)
letra = "" # Una letra individual de la frase
frase = "" # Frase que pediremos por teclado

# Programa principal.

system("cls") #Ejecuta el comando "cls"

frase = input("Teclea la frase: ")

for letra in frase: # Recorro toda la frase como una lista
    if letra != " ":
         if letra in letras: # Miro si la letra esta dentro de las claves del diccionario 
            letras[letra] += 1 # Aumento en 1 el numero de pariciones de la letra.
         else:
            letras[letra] = 1 # Añado la letra por primera vez

for letra in letras:
    print(f"La letra {letra} aparece {letras[letra]}.")