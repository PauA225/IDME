"""Programa que introduzca por teclado el valor de la nota de un examen y diga si está aprobado o suspenso (>=5).
Mejora: Vamos a repetir el proceso hasta introducir el valor 0"""

#Declaracion de Variables.

calificacion= 100 #Variable que da el valor de la nota del examen

#Programa principal.

while calificacion != 0:
    calificacion = float(input("Teclea el valor de la nota del examen: "))
    
    if calificacion >= 5:
        print("El examen está aprobado")
    
    else:
        print("Nos vemos en las recuperaciones")

    