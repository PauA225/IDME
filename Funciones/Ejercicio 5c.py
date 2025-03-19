"""Programa que, al introducir un valor numérico natural por teclado, nos diga si es  un número primo o no."""

# Importacion de librerías:

from os import system

# Declaracion de Variables.

numero = 0 # Contendra el valor a comprobar.

# Definicion de funciones.

def esPrimo(numero):
    for i in range(2, numero):
        if numero % i == 0: # Si el resto de la diision es 0, no es primo 
            return False # Devuelvo0 False por no ser primo
    return True # Si llega a este punto implica que los restos no son 0.

# Programa principal.

system("cls") #Ejecuta el comando "cls"

numero = int(input("Introduce el valor que quieres comprobar si es primo: "))
if esPrimo(numero) == True:
    print("El numero introducido es primo")
else:
    print("El numero introducido NO es primo")