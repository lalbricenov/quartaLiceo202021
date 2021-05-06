import matplotlib.pyplot as plt
import math

def f1(x):
    return abs(math.sin(10*x))*math.exp(-x**2)

# extremos del intervalo. Quiero hacer la grafica entre a y b
a = -4
b = 5

N = 10000 # numero de puntos que se van a calcular en el intervalo
dx = (b-a)/(N - 1)

# en C> for(int n = 0; n < N; n++)
# range(N)> corresponde a los numeros de 0 a N-1: [0,1,2,3,..., N-1]
# range(550, 1000) -> [550, 551, 552, ..., 999]
# range(550, 1000, 2) -> [550, 552, 554, ... , 998]
valsX = []#al inicio es un array vacio
valsY = []

for n in range(N):
    valsX.append(a + n * dx)
    valsY.append( f1(a + n * dx) )
    # print(n)
# print(valsX)
# print(valsY)

# Para calcular la derivada hago la resta entre 2 puntos consecutivos
# en y, y la divido entre la resta de las x

valsXD = []
valsYD = []
for n in range(N-1):
    valsXD.append( a + n * dx )
    # para calcular el valor de la derivada hago (yN+1 - yN)/(xN+1 - xN)

    valsYD.append( (valsY[n+1] - valsY[n]) / (valsX[n+1]- valsX[n]) )

# print(valsXD)
# print(valsYD)

plt.plot(valsX, valsY)
plt.plot(valsXD, valsYD)
plt.ylabel('x^2')
plt.xlabel('x')
plt.grid()
plt.savefig("x^2.jpg")

# plt.figure() #esto genera una figura nueva
# # Grafica con el numero de puntos preciso
# # Grafica de 2e^(-x^2) entre -3 y 3. La grafica debe tener 1500 puntos
# def f2(x):
#     return 2*math.exp(-x**2)
#     # return 2*math.exp(-math.pow(x,2))
#     # return 2*math.pow(math.e, -math.pow(x,2))
# valsX = []
# valsY = []
# N = 1500
# x = -3
# paso = (3 - (-3) )/(N-1)
# n = 0
# while n < N:
#     valsX.append(x)
#     valsY.append(f2(x))
#     x = x + paso
#     n = n + 1

# plt.figure() #esto genera una figura nueva
# plt.ylim([0,1]) #esto limita el rango de la grafica en y
# #'o', markersize=1 indica que se van a usar puntos en cambio de lineas.
# plt.plot(valsX, valsY, 'o', markersize=1)
# plt.ylabel('Campana')
# plt.xlabel('x')
# plt.savefig("Gauss.jpg")