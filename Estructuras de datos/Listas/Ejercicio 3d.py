"""Programa que pedirá por teclado una palabra y hemos de decir si es un palíndromo o no."""

# Importacion de librerías:

from os import system

# Declaracion de Variables.

palabra = "" # Contendra la palabra a identificar
i = 1 # Indice para recorrer la palabra, como una lista.
numVeces = 0 # Numero de veces a iterar en las comparaciones de letras.

# Programa principal.

system("cls") #Ejecuta el comando "cls"

palabra = input("Introduce la palabra a comprobar: ")

palabra = palabra.lower() # Convierto la palabra a minusculas.
if len(palabra) % 2 == 1: # Longitud de palabra impar
    numVeces = len(palabra) / 2 - 1
else:
    numVeces = len(palabra) / 2

while i <= numVeces and palabra[i-1] == palabra[-i]:
    i = i + 1

if i > numVeces and palabra[i-1] == palabra[-i]: #Ha salido del bucle con todas las comprobaciones correctas
   print(f"La palabra {palabra} ES un palindromo.")
else:
    print(f"La palabra {palabra} NO ES un palindromo.")
    