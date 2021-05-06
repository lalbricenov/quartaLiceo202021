import matplotlib.pyplot as plt
import math

def f1(x):
    return x**2 + math.cos(x) - 2 * math.exp(x)
# extremos del intervalo. Quiero hacer la grafica entre a y b
a = -2
b = 1
N = 10000 # numero de puntos que se van a calcular en el intervalo
dx = (b-a)/(N - 1)

valsX = []#al inicio es un array vacio
valsY = []

for n in range(N):
    valsX.append(a + n * dx)
    valsY.append( f1(a + n * dx) )
    # print(n)

plt.plot(valsX, valsY)
plt.xlabel('x')
plt.grid()
plt.savefig("f1.jpg")
