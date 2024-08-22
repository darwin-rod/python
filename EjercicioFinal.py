# Definimos la lista de compras vacía
lista_compras = []

# Función para mostrar el menú
def mostrar_menu():
    print("\n--- Administrador de Lista de Compras ---")
    print("1. Agregar artículo")
    print("2. Eliminar artículo")
    print("3. Ver artículos")
    print("4. Ordenar artículos alfabéticamente")
    print("5. Ordenar artículos por cantidad")
    print("6. Salir")

# Función para agregar un artículo
def agregar_articulo():
    nombre = input("Ingrese el nombre del artículo: ").capitalize()
    cantidad = int(input("Ingrese la cantidad: "))
    lista_compras.append({"nombre": nombre, "cantidad": cantidad})
    print(f"{cantidad} x {nombre} añadido a la lista.")

# Función para eliminar un artículo
def eliminar_articulo():
    nombre = input("Ingrese el nombre del artículo a eliminar: ").capitalize()
    for articulo in lista_compras:
        if articulo["nombre"] == nombre:
            lista_compras.remove(articulo)
            print(f"{nombre} eliminado de la lista.")
            return
    print(f"{nombre} no se encontró en la lista.")

# Función para ver los artículos
def ver_articulos():
    if not lista_compras:
        print("La lista de compras está vacía.")
    else:
        print("\nLista de Compras:")
        for articulo in lista_compras:
            print(f"{articulo['cantidad']} x {articulo['nombre']}")

# Función para ordenar alfabéticamente
def ordenar_alfabeticamente():
    lista_compras.sort(key=lambda x: x["nombre"])
    print("Lista ordenada alfabéticamente.")
    ver_articulos()

# Función para ordenar por cantidad
def ordenar_por_cantidad():
    criterio = input("Ordenar por cantidad ascendente (A) o descendente (D)? ").upper()
    if criterio == 'A':
        lista_compras.sort(key=lambda x: x["cantidad"])
        print("Lista ordenada por cantidad (ascendente).")
        ver_articulos()
    elif criterio == 'D':
        lista_compras.sort(key=lambda x: x["cantidad"], reverse=True)
        print("Lista ordenada por cantidad (descendente).")
        ver_articulos()
    else:
        print("Opción no válida.")

# Función principal
def ejecutar():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_articulo()
        elif opcion == "2":
            eliminar_articulo()
        elif opcion == "3":
            ver_articulos()
        elif opcion == "4":
            ordenar_alfabeticamente()
        elif opcion == "5":
            ordenar_por_cantidad()
        elif opcion == "6":
            print("¡Gracias por usar el Administrador de Lista de Compras!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

# Ejecutamos el programa
ejecutar()
