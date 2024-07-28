# Escriba las tablas de multiplicar de un número ingresado por el usuario la tabla debe multiplicar hasta el 15

numero_base =int(input("Ingrese numero para calcular tabla de multiplicar: "))

for i in range(1,16,1):
    print(numero_base,"*",i,"= ",numero_base*i)
