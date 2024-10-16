"""Programa que sume los primeros N números pares"""

# Declaracion de valores:

numero = 0 # Numero par que aumentara de dos en dos.
contador = 0 # Valor para contar el total de numeros ( debe ser 50 )
suma = 0 # Para acumular la suma de los valores
valorFinal = 0 # Contendra el numero de valores a sumar

#Programa principal:

valorFinal = int(input("Introduce el numero de valores pares a sumar: "))

for numero in range(0,2*valorFinal,2):
    suma = suma + numero # Acumulo en la variable "suma" las sumas
    contador = contador + 1 #Tambien se puede escribir "contador +=1"
    
print(f"La suma total es: {suma}")
print(f"El numero de valores pares contados es: {contador}")