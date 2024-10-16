"""Programa que pida por teclado números, hasta que introduzca el 0. Posteriormente debe mostrar su suma y su producto."""

# Importacion de librerías:

from os import system

# Declaracion de Variables.

numero = 1 # Valores dados por teclado (Pueden ser decimales)
suma = 0 # Para acumula los numeros sumados
producto = 1 # Para acumular la multiplicacion de los numeros

# Programa principal.

system("cls") #Ejecuta el comando "cls"

while numero != 0:
    numero = float(input("Introduce el numero a multiplicar y sumar: "))
    suma = suma + numero
    if numero != 0:
         producto = producto * numero

print(f"La suma total de los numeros es {suma}")
print(f"La multiplicacion total es {producto}")