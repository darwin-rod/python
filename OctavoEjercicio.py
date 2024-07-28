# Escribir un programa que pida al usuario un número entero y muestre por pantalla un triángulo como el de más abajo.
numero_base = int(input("Ingrese Numero: "))
anterior = ''
for i in range(1,numero_base+1,1):
    if i%2==1:
        print(i,anterior)
        anterior =str(i)+' '+anterior