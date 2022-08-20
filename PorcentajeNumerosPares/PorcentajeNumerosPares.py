from time import time
import random as random
c = 0
inicio = time()
x = []
for i in range(10000):
    x.append(random.randint(0,10000))
    if x[i]%2==0:
        c+=1
    if c > 0:
        print("El porcentaje de números pares es: ", (c/10000)*100,"%")
    else:
        print("No se generaron números pares")

tiempo = time() - inicio
print("Tiempo de ejecución: ", tiempo)