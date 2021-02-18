suma = 0
for n in range(10001):
    suma += n
print(f"La suma de los primeros 10000 enteros es {suma}")

suma = 0
for n in range(101):
    suma += n*n
print(f"La suma de los primeros 100 cuadrados es {suma}")

suma = 0
for n in range(101):
    # print(n*n*pow(-1, n+1))
    suma += n*n*pow(-1, n+1)
print(f"La suma de los primeros 100 cuadrados con signos intercalados es {suma}")