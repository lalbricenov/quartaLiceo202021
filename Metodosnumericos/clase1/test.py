import matplotlib.pyplot as plt
import math
# plot(valoresX, valoresY)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'H')
plt.ylabel('Posición(m)')
plt.xlabel('Tiempo(s)')
plt.savefig("test.jpg")

# vamos a graficar la funcion sin(2x) entre 0 y 4 pi

def funcion1(x):
    return math.sin(2*x)

# construimos array para las x
valsX = [] #iniciamos con un array vacio para las x
valsY = [] #iniciamos con un array vacio para las y
x = 0
while x <= 4*math.pi:
    valsX.append(x)
    valsY.append(funcion1(x))
    x = x + 0.1


plt.figure() #esto genera una figura nueva
plt.plot(valsX, valsY)
plt.ylabel('sin(2x)')
plt.xlabel('x')
plt.savefig("seno.jpg")

# Grafica con el numero de puntos preciso
# Grafica de 2e^(-x^2) entre -3 y 3. La grafica debe tener 1500 puntos
def f2(x):
    return 2*math.exp(-x**2)
    # return 2*math.exp(-math.pow(x,2))
    # return 2*math.pow(math.e, -math.pow(x,2))
valsX = []
valsY = []
N = 1500
x = -3
paso = (3 - (-3) )/(N-1)
n = 0
while n < N:
    valsX.append(x)
    valsY.append(f2(x))
    x = x + paso
    n = n + 1

plt.figure() #esto genera una figura nueva
plt.ylim([0,1]) #esto limita el rango de la grafica en y
#'o', markersize=1 indica que se van a usar puntos en cambio de lineas.
plt.plot(valsX, valsY, 'o', markersize=1)
plt.ylabel('Campana')
plt.xlabel('x')
plt.savefig("Gauss.jpg")