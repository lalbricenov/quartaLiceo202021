# programa que calcula la integral de una función usando el método
# del trapecio.

# incluyo la libreria math
import math

# Defino la función a integrar:

def f(x):
    #return math.exp(x)
    return math.exp(-x**2)

# Defino los extremos y el valor de n
a = -0.5
b = 0.5
n = 2000
# Calculo el ancho de cada trapecio: h
h = (b-a)/n

# Hago la suma y obtengo el resultado
# h/2 * (f(x0) + 2*f(x1) + 2*f(x2) + ... + 2*f(xn-1) + f(xn))
resultado = 0
x = a
# print(f"Primero sumo f({x}) = {f(x)} ")
resultado += f(x)

for i in range(1, n):
    x = a + i * h
    # print(f"Sumo f({x}) = {f(x)}, que corresponde a i = {i}")
    resultado += 2*f(x) # resultado = resultado + 2 * f(x)

x = b
# print(f"Por último sumo f({x}) = {f(x)} ")
resultado += f(x)# resultado = resultado + f(x)

resultado = resultado * h / 2

print(f"La integral de e^(-x^2) entre {a} y {b} es {resultado}")