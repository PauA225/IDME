"""Programa en el que el usuario introduzca un número por teclado y se asegure que está entre 1 y 10 (ambos incluídos). 
Si no lo es, que vuelva a pedirlo hasta que lo sea. Al final, muéstralo en pantalla."""

# Importacion de librerías:

from os import system

# Declaracion de Variables.

numero = 0 # Numero que introducirá el usuario

# Programa principal.

system("cls") #Ejecuta el comando "cls"

while numero < 1 or numero > 10:
    numero = float(input("Introduce un numero entre el 1 y 10: "))
    
print(f"El numero introducido es {numero}")