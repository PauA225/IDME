"""Programa de Login que compruebe el usuario y contraseña en el diccionario a continuación:

	usuarios = {
	"aexposito":
	    {"nombre": "Antonio",
		    "apellidos": {"primerApellido": "Expósito", "segundoApellido": "Núñez"},
	    "password": "123456"},
	"fgonzalez":
	    {"nombre": "Francisco",
		    "apellidos": {"primerApellido": "González", "segundoApellido": "Martínez"},
	    "password": "jejejaja"},
	"lcastillo":
	    {"nombre": "Lourdes",
		    "apellidos": {"primerApellido": "Prieto", "segundoApellido": "Valverde"},
	    "password": "6789"}
	    }	
El usuario tendrá un máximo de 3 intentos, 
y al acceder correctamente se mostrará un mensaje de bienvenida, con el nombre y apellidos del usuario."""

# Importacion de librerías:

from os import system

# Declaracion de Variables.

usuarios = {
	"aexposito":
	    {"nombre": "Antonio",
		    "apellidos": {"primerApellido": "Expósito", "segundoApellido": "Núñez"},
	    "password": "123456"},
	"fgonzalez":
	    {"nombre": "Francisco",
		    "apellidos": {"primerApellido": "González", "segundoApellido": "Martínez"},
	    "password": "jejejaja"},
	"lcastillo":
	    {"nombre": "Lourdes",
		    "apellidos": {"primerApellido": "Prieto", "segundoApellido": "Valverde"},
	    "password": "6789"}
	    }
usuario = "" # Nombre de usuario que vamos a pedir por teclado
contraseña= "" # Codigo que pediremos por teclado.
numIntentos= 0 # Cuenta el numero de intentos
valido = False # Indicara si la combinacion de usuario y contraseña es valida

# Programa principal.

system("cls") #Ejecuta el comando "cls"

while numIntentos < 3 and valido == False:
    usuario = input("Introduce el usuario: ")
    contraseña = input ("Contraseña: ")
    numIntentos += 1
    if usuario in usuarios and contraseña == usuarios[usuario]["password"]:
        valido = True
        print(f"Bienvenid@ {usuarios[usuario]["nombre"]} {usuarios[usuario]["apellidos"]["primerApellido"]} {usuarios[usuario]["apellidos"]["segundoApellido"]}")
    else:
        print(f"La combinacionn de usuario y contraseña no es valido. Te quedan {3- numIntentos} intentos.")
        valido = False
        input("Pulsa ENTER para continuar")