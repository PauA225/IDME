"""Que muestre en pantalla los primeros 50 números pares"""

#Declaracion de variables:

numero= 0 # Para contar el numero de valores
contador= 0 # Va a contar el numero de  valores

#Programa principal:

for numero in range(0,100,2):
    print(numero)
    contador = contador + 1 #Tambien se puede escribir "contador +=1"

print(f"El numero de valors contados es: {contador}")