"""Programa que, reutilizando la función del apartado anterior, debemos indicar si son primos o no los valores numéricos de un rango introducido por teclado."""

# Importacion de librerías:

from os import system

# Declaracion de Variables.

numero = 0 # Numeros a comprobar.
limiteInferior = 0 # Limite inferior del rango introduicido.
limiteSuperior = 0 # Limite Superior del rango introduicido.

# Definicion de funciones.

def esPrimo(numero):
    for i in range(2, numero):
        if numero % i == 0: # Si el resto de la diision es 0, no es primo 
            return False # Devuelvo0 False por no ser primo
    return True # Si llega a este punto implica que los restos no son 0.

# Programa principal.

system("cls") #Ejecuta el comando "cls"

limiteInferior = int(input("Introduce el valor inferior del rango de numeros a comprobar si son primos: "))
limiteSuperior = int(input("Introduce el valor superior del rango de numeros a comprobar si son primos: "))

for numero in range(limiteInferior, limiteSuperior + 1):
    if esPrimo(numero) == True:
        print(f"El numero {numero} es primo")
    else:
        print(f"El numero {numero} NO es primo")