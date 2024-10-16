"""Programa que lea por teclado 2 números y diga cuál es mayor (supondremos que son diferentes)"""

# Importacion de librerías:

from os import system

#Declaracion de Variables.

numero1 = 0 # Primer valor escrito
numero2 = 0 # Segundo valor escrito

system("cls") #Ejecuta el comando "cls"

#Programa principal.

numero1 = int(input("Teclea el primer numero: "))
numero2 = int(input("Teclea el segundo numero: "))

if numero1 < numero2 :
    print("El primer numero es MENOR que el segundo")

else:
    print("El primer numero es MAYOR que el segundo")