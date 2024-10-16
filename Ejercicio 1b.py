"""Programa para convertir un valor en euros a dolares"""

#Declaracion de variables
euros=0 # Va a contener el valor en euros, que pedire por teclado
cambio=0 #Contiene el valor del cambio del dia (se pide por teclado)

#Programa principal.
cambio= float(input("Dime el cambio del dia de euros a dolares: ")) #Utilizamos el Float para numeros decimales en vez de int
euros= int(input("Introduce el valor de euros a convertir a dolares: "))
print("El valor en dolares es ", cambio*euros)