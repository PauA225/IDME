"""Programa que sume todos los números pares positivos, partiendo desde 0, hasta que la suma supere el valor de 1000. 
Posteriormente, debe mostrar en pantalla cuál es el valor de la suma y cuántos números se han sumado."""

# Importacion de librerías:

from os import system

# Declaracion de Variables.

suma = 0 # Acumulacion de numeros sumados
numero = 0 # Valores pares que van a sumarse
contador = 0 # Numero de valores que se han sumado

# Programa principal.

system("cls") #Ejecuta el comando "cls"

while suma <= 1000:
    suma = suma + numero
    numero += 2 # Equivale a escribir numero = numero + 2
    contador += 1 # Equivale a escribir contador = contador + 1

print(f"La suma es {suma}")
print(f"El numero de valores sumados es: {contador}")