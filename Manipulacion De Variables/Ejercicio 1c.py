"""Resuelve una ecuación de 2º grado, ax2+bx+c = 0,
introduciendo los coeficientes a, b y c."""

#Importacion de librerias
from math import sqrt

#Declaracion de variables:
a = 0 # Coeficiente del termino de segu8ndo grado
b = 0 # Coeficiente del termino en primer grado
c = 0 # Termino independiente
x1 = 0 # Solucion con el "+"
x2 = 0 # Solucion con el "-"

# Programa principal:

print("Ecuacion de segundo grado: ax^2+bx+c=0")
a = float(input("Teclea el coeficiente del termino de segundo grado (a): "))
b = float(input("Teclea el coeficiente del termino de primer grado (b): "))
c = float(input("Teclea el termino independiente (c): "))

print(f"Ecuacion de segundo grado: {a}x^2+{b}x+{c}= 0")

x1 = (-b+sqrt(b**2-4*a*c)) / (2*a)
x2 = (-b-sqrt(b**2-4*a*c)) / (2*a)

print(f"Las soluciones son: x1={x1} y x2={x2}")