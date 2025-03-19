"""Programa que pida por teclado una serie de asignaturas, con su calificación correspondiente, hasta que introduzca una asignatura en blanco. 
Posteriormente nos debe mostrar por pantalla la lista de las que están aprobadas (calificación mayor o igual que 5),
con su correspondiente nota y la media aritmética de todas las calificaciones (se incluirán también las notas suspensas en la media).
Utilizando diccionarios"""

# Importacion de librerías:

from os import system

# Declaracion de Variables.

asignaturas = {} # Diccionario que contendra los datos (nombre y nota)
nombreAsignatura = " "
calificacion = 0 # Contendra la nota con decimales incluidos
sumaClasificaciones = 0 # Para hacer la media aritmetica

# Programa principal.

system("cls") #Ejecuta el comando "cls"

while nombreAsignatura != "" : # Bucle para pedir las asignaturas
    nombreAsignatura = input("Teclea la asignatura (ENTER para finalizar): ")
    if nombreAsignatura != "":
        calificacion = float(input("Introduce la calificacion de la asignatura: "))
        asignaturas[nombreAsignatura] = calificacion
    print("") # Salto de linea para separar asignaturas

for nombreAsignatura in asignaturas:
    if asignaturas[nombreAsignatura] >= 5:
        print(f"La asignatura {nombreAsignatura} esta aprobada con un {asignaturas[nombreAsignatura]}")
    sumaClasificaciones = sumaClasificaciones + asignaturas[nombreAsignatura]

print("") # Salto de linea
print(f"La media aritmetica es {sumaClasificaciones/len(asignaturas)}")