# Ingrese a una serie de números por teclado e indique cuál es el mayor. 
# Para terminar el programa el usuario debe ingresar el valor 0 (cero).

numero = -1
while numero != 0:
    numero_uno = int(input("Ingrese un primer numero: ")) 
    if numero_uno == 0: break
    numero_dos = int(input("Ingrese un segundo numero: "))
    if numero_dos == 0: break
    if numero_uno > numero_dos:
        print("El número uno ", numero_uno, "es mayor que el numero dos ", numero_dos)
    else:
        print("El número dos ", numero_dos, "es mayor que el numero uno ", numero_uno)