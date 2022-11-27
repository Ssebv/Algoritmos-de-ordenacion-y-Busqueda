import random
import time
import matplotlib.pyplot as plt

#funcion que busca en forma secuencial en una lista
def buscar_secuencial(lista, elemento):    
    for (idx, item) in enumerate(lista):
        time.sleep(0.01) #esto hace que "artificalmente" demore más
        if item  == elemento:
            return idx
    
    return -1; # si no lo encuentra, devuelve -1

#Tamaño inicial del problema
N = 10
tiempo = []
muestra = []

for i in range(0,15):
    
    lista = [random.randint(0, 100) for iter in range(N)]
    #buscamos un elemento que existe en la lista
    ini = time.time()
    buscar_secuencial(lista, random.randint(0, 100))
    muestra.append(N)
    fin = time.time()
    tiempo.append(fin-ini)
    
    N = N*2

#print(tiempo)
#print(indice)

plt.plot(tiempo,muestra, 'ro')
plt.axis([0,max(tiempo) + 2, 0, max(muestra)])
plt.xlabel('Tiempo')
plt.ylabel('Tamaño de la muestra')
plt.title('Tiempo del algoritmo de busqueda secuencial')
plt.show()


#imprime el indice del numero (si es encontrado)
#print("Indice %d" % )
#print("Tiempo %f" % (tiempo))
