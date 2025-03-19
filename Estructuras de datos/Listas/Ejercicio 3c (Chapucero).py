"""Programa en el que introduciremos por teclado una matriz de 2 x 2, y nos devolverá el valor de su determinante. """

# Importacion de librerías:

from os import system

# Declaracion de Variables.

matriz = [[0, 0],[0, 0]] # La lista que contendra los elementos de la matriz.
numero = 0 # Contiene el valor de las variables.
determinante = 0 # Contiene el valor de la solucion.

# Programa principal.

system("cls") #Ejecuta el comando "cls"

matriz[0][0] = float(input("Teclea la posicion superior izquierda de la matriz: "))
matriz[0][1] = float(input("Teclea la posicion superior derecha de la matriz: "))
matriz[1][0] = float(input("Teclea la posicion inferior izquierda de la matriz: "))
matriz[1][1] = float(input("Teclea la posicion inferior derecha de la matriz: "))
determinante = matriz[0][0] * matriz[1][1] - matriz[1][0] * matriz[0][1]

print(f"La solucion del determinante de la matriz es: {determinante}.")