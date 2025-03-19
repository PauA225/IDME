"""Programa que escriba una función que reciba como parámetro una cadena de palabras separadas por espacios (frase) y devuelva, 
como resultado, cuántas palabras de más de cinco letras tiene la cadena dada."""

# Importacion de librerías:

from os import system

# Declaracion de Variables.

frase = ""
letra = 0 
j = 0 # Incluye el numero de letras por palabra
contadorPalabras = 0 # Cuenta las palabras de mas de 4 letras
# Definicion de funciones.

def contarPalabras (frase):
    letra = 0 
    j = 0 # Incluye el numero de letras por palabra
    contadorPalabras = 0 # Cuenta las palabras de mas de 4 letras

    for letra in frase: # Recorro toda la frase
        if letra == " ": # Si la letra es un espacio
            if j > 4:
                contadorPalabras = contadorPalabras + 1
            j = 0
        j = j + 1
    
    if j > 4:
        contadorPalabras += 1 
    
    return contadorPalabras

# Programa principal.

system("cls") #Ejecuta el comando "cls"

frase = input("Introduce la frase a comprobar: ")
print(contarPalabras(frase))