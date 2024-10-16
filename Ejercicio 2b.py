"""Que sume los primeros 50 números impares"""

# Declaracion de valores:

numero= 0 # Numero impar que aumentara de dos en dos.
contador = 0 # Valor para contar el total de numeros ( debe ser 50 )
suma= 0 # Para acumular la suma de los valores

#Programa principal:

for numero in range(1,100,2):
    suma = suma + numero # Acumulo en la variable "suma" las sumas
    contador = contador + 1 #Tambien se puede escribir "contador +=1"
    
print(f"La suma total es: {suma}")
print(f"El numero de valores impares contados es: {contador}")