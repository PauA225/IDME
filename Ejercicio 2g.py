"""(Estructura “elif”) Programa que pide por teclado un valor entre 1 y 7 y 
debe indicarnos por pantalla el día de la semana correspondiente"""

# Importacion de librerías:

from os import system

# Declaracion de Variables.

diasSemana = 0 #Contendra el numero que se tranformara a dia de la semana

# Programa principal.

system("cls") #Ejecuta el comando "cls"

diasSemana = int(input("Introduce el numero del dia de la semana: "))

if diasSemana == 1 :
    print("Has introducido Lunes")
elif diasSemana == 2 :
    print("Has introducido Martes")
elif diasSemana == 3 :
    print("Has introducido Miercoles")
elif diasSemana == 4 :
    print("Has introducido Jueves")
elif diasSemana == 5 :
    print("Has introducido Viernes")
elif diasSemana == 6 :
    print("Has introducido Sábado")
elif diasSemana == 7 :
    print("Has introducido Domingo")
else:
    print("Introduce un valor comprendido entre 1-7")