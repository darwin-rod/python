#     Un restaurante italiano ofrece pizzas vegetarianas y no vegetarianas a sus clientes. 
# Los ingredientes para cada tipo de pizza aparecen a continuación.
#         Tipos pizza vegetarianos:
#             Tipo 1: Pimiento, tofu
#             Tipo 2 Salsa de tomate, cebolla
#             Tipo 3: Champiñones, brócoli.
#             Tipo 4: 7 Quesos
#         Tipos no vegetarianos:
#             Tipo 1: Peperoni, Carne
#             Tipo 2: Pollo, Jamón
#             Tipo 3: Salchichón Italiano, Salami  

# Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, 
# y en función de su respuesta le muestre un menú con los tipos disponibles para que elija. Solo se puede eligir un  tipo de Pizza.

# Al final se debe mostrar por pantalla si la pizza elegida es vegetariana o no y todos los ingredientes que lleva.
mensaje_vegetariana= "Escogió una pizza vegetariana con los siguientes ingredientes"
mensaje_no_vegetariana= "Escogió una pizza no vegetariana con los siguientes ingredientes"
opcion = input("Desea una Pizza Vegetariana S (si) / N (no): ")

if opcion == 'S':
    print("1.- Tipo 1 \n 2.- Tipo 2 \n 3.- Tipo 3 \n 4.- Tipo 4")
else :
    print("1.- Tipo 1 \n 2.- Tipo 2 \n 3.- Tipo 3")

tipo = input("Escoja un numero de pizza: ")

if opcion == 'S' and tipo == '1':
    print(mensaje_vegetariana," Pimiento, tofu")
elif opcion == 'S' and tipo == '2':
    print(mensaje_vegetariana," Salsa de tomate, cebolla")
elif opcion == 'S' and tipo == '3':
    print(mensaje_vegetariana," Champiñones, brócoli")
elif opcion == 'S' and tipo == '4':
    print(mensaje_vegetariana," 7 Quesos")
elif opcion == 'N' and tipo == '1':
    print(mensaje_no_vegetariana," Peperoni, Carne")
elif opcion == 'N' and tipo == '2':
    print(mensaje_no_vegetariana," Pollo, Jamón")
elif opcion == 'N' and tipo == '3':
    print(mensaje_no_vegetariana," Salchichón Italiano, Salami")
else:
    print("Error: No tenemos esa pizza, revisar opciones.")
