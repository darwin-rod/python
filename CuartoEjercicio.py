# Al recibir como datos un grupo de números enteros positivos, para terminar el 
# ciclo el usuario deberá ingresar el número cero (0), calcule el cuadrado de 
# estos números. Imprima el cuadrado de los números recibidos y al final la suma de los cuadrados.
numero = -1
suma = 0
while numero != 0:
    numero = int(input("Ingrese un numero: "))
    if numero == 0:
        continue
    print("El cuadrado del número ingresado es: ", numero*numero)
    suma = suma + numero
print("La suma de todos los numeros ingresados es: ", suma)
