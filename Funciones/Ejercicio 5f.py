"""Programa que cree una función que aplique un descuento a un precio dado. Tomará dos parámetros, el precio y el porcentaje de descuento. 
Devolverá el importe del precio con el descuento aplicado.
Valida que el descuento esté entre 0 y 100. En caso contrario, imprime mensaje de error y devuelve -1
Añade un parámetro opcional, llamado “impuestos”, que será el porcentaje de impuestos a aplicar. 
En caso de no utilizar el parámetro, se entenderá que no hay impuestos a aplicar.
"""

# Importacion de librerías:

from os import system

# Declaracion de Variables.

precio = 0 
porcentajeDescuento = 0 
porcentajeImpuestos = 0

# Definicion de funciones.

def calculoImporte(precio, descuento, impuesto = 0):
    if descuento < 0 or descuento > 100:
        print("ERROR: El porcentaje no esta bien aplicado")
        return -1
    return precio * (1 - descuento / 100) * (1 + impuesto / 100)

# Programa principal.

system("cls") #Ejecuta el comando "cls"

precio = float(input("Introduce el precio del articulo: "))
porcentajeDescuento = float(input("Introduce el porcentaje de decuento a aplicar: "))
porcentajeImpuestos = input("Introduce el porcentaje de impuestos (ENTER si no aplica):  ")

if porcentajeImpuestos == "":
    print(f"El importe final es: {calculoImporte(precio,porcentajeDescuento)}")
else:
    print(f"El importe final es: {calculoImporte(precio, porcentajeDescuento, float(porcentajeImpuestos))}")