"""Programa en el que introduciremos por teclado una matriz de 2 x 2, y nos devolverá el valor de su determinante. """

# Importacion de librerías:

from os import system

# Declaracion de Variables.

matriz = [[0, 0],[0, 0]] # La lista que contendra los elementos de la matriz.
fila = 0 # Contiene el valor de la fila.
columna = 0 # Contiene el valor de la columna.
determinante = 0 # Contiene el valor de la solucion.

# Programa principal.

system("cls") #Ejecuta el comando "cls"
for fila in range(0,2): # Recuerda que range llega hasta un valor por debajo del 2º parametro.
    for columna in range(0,2):
        matriz[fila][columna] = float(input(f"Teclea la posicion fila {fila}, columna {columna} de la matriz: "))

determinante = matriz[0][0] * matriz[1][1] - matriz[1][0] * matriz[0][1]

print(f"La solucion del determinante de la matriz es: {determinante}.")