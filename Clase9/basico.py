# Variables
x = 2
y = 4.5
nombre = "Quarta"
# f strings:formatted strings como en C
print(f"El tipo de variable de x es {type(x)} y su valor es {x}")
print(f"El tipo de variable de y es {type(y)} y su valor es {y}")
print(f"El tipo de variable de nombre es {type(nombre)} y su valor es {nombre}")

notas = [3, 5.4, 6.9, 9.3, 9.4, 9.6]
print(f"El tipo de variable de notas es {type(notas)} y su valor es {notas}")
print(f"El tipo de variable la primera nota es {type(notas[0])} y su valor es {notas[0]}")
print(f"El tipo de variable la segunda nota es {type(notas[1])} y su valor es {notas[1]}")

estudiante = {"nombre":"Juan", "apellido":"Rodriguez", "edad":59, "notas":[6.7, 9.4, 7.5, 6.3 ]}
# El apellido de Juan es Rodriguez, su edad es 59 y el promedio de sus notas es

print(f"El apellido de {estudiante['nombre']} es {estudiante['apellido']} y su edad es {estudiante['edad']} y el promedio de sus notas es {sum(estudiante['notas'])/len(estudiante['notas']):.2f}")

# OPERADORES
# aritmeticos
x=3
y=4.5
z=17
print(f"Division: {z/x}")
print(f"Modulo (residuo): {z % x}")

# logicos
a = True
b = False
# tabla de verdad del and
print("TABLA DE VERDAD DEL AND")
print(f"T and T: {True and True}")
print(f"T and F: {True and False}")
print(f"F and T: {False and True}")
print(f"F and F: {False and False}")

# tabla de verdad del or
print("TABLA DE VERDAD DEL OR")
print(f"T or T: {True or True}")
print(f"T or F: {True or False}")
print(f"F or T: {False or True}")
print(f"F or F: {False or False}")
#print(f"And: {a and b}")
#print(f"Or: {a or b}")
