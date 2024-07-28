# Recibir un número positivo N, comenzando desde 10 hasta N 
# obtenga la suma de los números pares y el promedio de los impares.
suma_par= 0
suma_impar= 0
contador = 0
promedio= 0
numero = int(input("Ingrese un numero mayor a 10: "))

if numero <= 10: 
    print("Ingrese un numero mayor a 10")
else:
    for i in range(10,numero):
        if i%2 == 0:
            suma_par = suma_par + i
        else:
            suma_impar = suma_impar + i
            contador +=1
    promedio = suma_impar / contador
    print("La suma de los numeros pares: ", suma_par)
    print("El promedio de los numeros impares es: ", promedio)
