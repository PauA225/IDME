"""Programa que creara una función que nos devuelva True si un valor parámetro está dentro de un rango, 
que también introduciremos como parámetros. Si no es así, devolverá False."""

# Importacion de librerías:

from os import system

# Declaracion de Variables.

numero = 0 # Contendra el valor a comprobar.
limiteInferior = 0 # Valor del limite inferior del intervalo.
limiteSuperior = 0 # Valor del limite superior del intervalo.

# Definicion de funciones.

def intervalo(num, limInferior, limSuperior):
    if num >= limInferior and num <= limSuperior:
        return True
    else:
        return False

# Programa principal.

system("cls") #Ejecuta el comando "cls"

numero = int(input("Teclea el numero a comprobar: "))
limiteInferior = int(input("Introduce el limite inferior del intervalo: "))
limiteSuperior = int(input("Introduce el limite superior del intervalo: "))

if intervalo (numero, limiteInferior, limiteSuperior):
    print("El valor esta dentro del intervalo.")
else:
    print("El valor no esta dentro del intervalo.")