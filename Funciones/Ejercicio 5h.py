"""Programa que devuelva el valor de una resistencia de 4 bandas, indicando su intervalo. Habrá que pasarle los colores de las 4 bandas."""

# Importacion de librerías:

from os import system

# Declaracion de Variables.

color1, color2, color3, color4 = 0, 0, 0, 0 # Colores que se pediran por teclado
colores = {"Negro": 0, "Marron": 1, "Rojo": 2, "Naranja": 3, "Amarillo": 4, "Verde": 5, "Azul": 6, "Violeta": 7, "Gris": 8, "Blanco": 9,}
coloresTolerancias = {"Rojo": 2, "Dorado": 5, "Plata": 10}
resultado = []

# Definicion de funciones.

def resistencia(color1, color2, color3, color4):
    coloresValor = {"Negro": 0, "Marron": 1, "Rojo": 2, "Naranja": 3,
               "Amarillo": 4, "Verde": 5, "Azul": 6, "Violeta": 7,
               "Gris": 8, "Blanco": 9,}

    coloresTolerancias = {"Rojo": 2, "Dorado": 5, "Plata": 10}
    
    valorNominal = (coloresValor[color1] * 10 + coloresValor[color2]) * 10**coloresValor[color3]
    limiteInferior = valorNominal - coloresTolerancias[color4] / 100 * valorNominal
    limiteSuperior = valorNominal + coloresTolerancias[color4] / 100 * valorNominal
    return (valorNominal, limiteSuperior, limiteInferior)

# Programa principal.

system("cls") #Ejecuta el comando "cls"

color1 = input("Teclea el color de la primera banda: ")
color2 = input("Teclea el color de la segunda banda: ")
color3 = input("Teclea el color de la tercera banda: ")
color4 = input("Teclea el color de la cuarta banda: ")

color1 = color1.capitalize()
color2 = color2.capitalize()
color3 = color3.capitalize()
color4 = color4.capitalize()

resultado = resistencia(color1, color2, color3, color4)

print(f"El valor nominal es: {resultado[0]}")
print(f"El intervalo es: {resultado[1]}, {resultado[2]}")