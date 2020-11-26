# condicionales, bucles y funciones
# condicionales
x = 0
if x % 2 == 0:
    print("x es par")
else:
    print("x es impar")

if x > 0:
    print("x es positivo")
else:
    if x < 0:
        print("x es negativo")
    else:
        print("x es cero")

## segunda manera, usando elif
if x > 0:
    print("x es positivo")
elif x < 0: ## se va a llegar  a esta linea solo si x no es mayor a cero
    print("x es negativo")## se llega a esta line si x no es mayor a cero
    ## y x es menor a cero
else:
    print("x es cero") # se llega a esta linea si x no es mayor a cero
    # y x no es menor a cero

sexo = "M"
edad = 15

if sexo == 'F' and edad > 12:
    print("La persona es una mujer mayor a 12 años")
else:
    print("La persona no es una mujer o no es mayor a 12 años")

## Bucles
# while
# != diferente
## imprimir todos números de 1 en 1, hasta que alguno sea multiplo de 7
# y múltiplo de 17
# n = 1
# while n % 7 != 0 or n % 17 != 0:
#     print(n)
#     n = n + 1

# for

# for i in range(-5,50,2):
# for i in range(21):
#     # print(i*i)
#     print('Hola quarta')

pedro = {"nombre":"Pedro Antonio","apellido":"Perez Rodriguez", "edad": 67,"notas":[6.7,8.5, 9.6, 10, 4.3, 6.2]}
juan = {"nombre":"Juan Antonio","apellido":"Perez Rodriguez", "edad": 65,"notas":[6.7,8.5, 9.6, 10, 4.3, 6.2]}
# print(f'Nombre: {pedro["nombre"]} {pedro["apellido"]}')
# print(f'Edad: {pedro["edad"]}')

# for i in range(len(pedro["notas"])):
#     print(f'Nota {i+1}: {pedro["notas"][i]}')

# for nota in pedro["notas"]:
#     print(nota)

# Funciones
def imprimirEstudiante(estudiante):
    print(f'Nombre: {estudiante["nombre"]} {estudiante["apellido"]}')
    print(f'Edad: {estudiante["edad"]}')

    for i in range(len(estudiante["notas"])):
        print(f'Nota {i+1}: {estudiante["notas"][i]}')

imprimirEstudiante(pedro)
imprimirEstudiante(juan)
