import time
import random
import matplotlib.pyplot as plt

#funcion que busca un numero en una lista (la lista debe estar ordenada)
def buscar_binaria(lista, elemento):
    pos = -1
    izq = 0
    der = len(lista)-1
    while pos==-1 and izq<=der:
        medio=int((izq+der)/2);
        if lista[medio] == elemento:
            pos = medio;
        elif lista[medio] > elemento:
            der = medio-1;
        else:
            izq = medio+1;
    return pos;

#Tamaño inicial del problema
N = 10
tiempo = []
muestra = []

for i in range(0,15):
    
    lista = [*range(0,N,3)]
    #buscamos un elemento que existe en la lista
    ini = time.time()
    buscar_binaria(lista, random.randint(0, N))
    muestra.append(N)
    fin = time.time()
    tiempo.append(fin-ini)
    N = N*2

#print(tiempo)

plt.plot(tiempo,muestra, 'ro')
plt.axis([0,max(tiempo),0, max(muestra)])
plt.xlabel('Tiempo')
plt.ylabel('Tamaño de la muestra')
plt.title('Tiempo del algoritmo de busqueda binaria')
plt.show()
