"""Programa que simule una lista de compras. El programa debe permitir al usuario realizar las siguientes operaciones:
Agregar un artículo a la lista de compras.
Eliminar un artículo de la lista de compras.
Mostrar los artículos que están actualmente en la lista.
Salir del programa."""

# Importacion de librerías:

from os import system

# Declaracion de Variables.

listacompra = [] #Lista que va a contener los articulos
opciones = 0 #Contiene la opcion que se escogera por teclado
articulo = "" #Nombre de los articulos

# Programa principal.

system("cls") #Ejecuta el comando "cls"

while opciones != 4:

    system("cls")

    print("") # Salto de línea para dejar una línea en blanco.
    print("***************   MENÚ PRINCIPAL  ****************")
    print("1.- Agregar un artículo a la lista de la compra.")
    print("2.- Eliminar un artículo a la lista de la compra.")
    print("3.- Mostar todos los artículos de la lista de la compra.")
    print("4.- Salir del programa")
    print("") # Hago un salto de línea.
    opciones = int(input("Elige la opción correspondiente... "))

    if opciones == 1:
        print("") # Hago un salto de línea.
        articulo = input("Introduce el nombre del nuevo artículo: ")
        articulo = articulo.capitalize()
        if articulo in listacompra:
            print(f"Error: El artículo {articulo} ya se encuentra en la lista")
            print("") # Hago un salto de línea.
            input("Pulsa una tecla para continuar...")
        else:
            listacompra.append(articulo)
            print(f"El artículo '{articulo}' ha sido añadido a la lista correctamente")
            print("") # Hago un salto de línea.
            input("Pulsa una tecla para continuar...")
    if opciones == 2:
        print("") # Hago un salto de línea.
        articulo = input("Introduce el nombre del artículo que quiere borrar: ")
        articulo = articulo.capitalize()
        if articulo in listacompra:
            listacompra.remove(articulo)
            print(f"El artículo '{articulo}' ha sido eliminado de la lista correctamente")
            print("") # Hago un salto de línea.
            input("Pulsa una tecla para continuar...")
        else:
            print(f"Error: El artículo {articulo} no se encuentra en la lista")
            print("") # Hago un salto de línea.
            input("Pulsa una tecla para continuar...")
    if opciones == 3:
        print("") # Hago un salto de línea.
        print("Lista de compra: ")
        for nombre in listacompra:
            print(f"-{nombre}.")
        print("") # Hago un salto de línea.
        input("Pulsa una tecla para continuar...")

print("**********PROGRAMA CERRADO***************")