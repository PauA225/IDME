"""Programa que cree un diccionario simulando una cesta de la compra. 
El programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta que el usuario decida terminar. 
Después se debe mostrar por pantalla la lista de la compra y el coste total."""

# Importacion de librerías:

from os import system

# Declaracion de Variables.

compra = {} # Lista donde meteemos los productos
producto = " " # Nombre del producto
precio = 0 # Precio de los productos
precioTotal = 0 # Suma de los precios

# Programa principal.

system("cls") #Ejecuta el comando "cls"

while producto != "" : # Bucle para pedir los productos
    producto = input("Teclea el producto (ENTER para finalizar): ")
    if producto != "":
        precio = float(input("Introduce el precio del producto: "))
        compra[producto] = precio
    print("") # Salto de linea para separar productos.

print("***** Lista de la compra *****")
print("")
for producto in compra:
    print(f"Articulo: {producto}, precio: {compra[producto]}")
    precioTotal = precioTotal + compra[producto]

print("")
print(f"Importe total compra: {precioTotal}")