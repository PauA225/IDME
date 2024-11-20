"""Programa que pedirá por teclado la lista de los números de la lotería de los últimos 7 días. 
Posteriormente los mostrará ordenados de menor a mayor y de mayor a menor. """

# Importacion de librerías:

from os import system

# Declaracion de Variables.

listaloteria = [] # La lista que contendra todos los elementos.

numero = 0 # Contiene el valor del numero de la loteria

# Programa principal.

system("cls") #Ejecuta el comando "cls"

for indice in range (0,7) :
    numero = int(input(f"Introduce el {indice + 1}º numero de la loteria: "))
    listaloteria.append (numero)

print("Lista desordenada...")
print(listaloteria)

listaloteria.sort()
print("Lista de loteria ordenada...")
print(listaloteria)

listaloteria.sort(reverse = False)
print("Lista ordenada de menor a mayor...")
print(listaloteria)

listaloteria.sort(reverse = True)
print("Lista ordenada de mayor a menor")
print(listaloteria)