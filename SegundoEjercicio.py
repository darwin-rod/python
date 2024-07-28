# Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y el nombre. 
# El grupo A esta formado por las mujeres con un nombre anterior a la M y los hombres con un nombre posterior a la 
# N y el grupo B por el resto. 
# Escribir un programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo que le corresponde.

nombre = input("Ingrese su nombre: ")
sexo   = input("Ingrese su sexo F (femenino) / M (masculino): ")

primera_letra= nombre[0]

if (primera_letra < 'M' and sexo == 'F') or (sexo == 'M' and primera_letra > 'N'):
    print("Usted pertenece al grupo A")
else:
    print("Usted pertenece al grupo B")