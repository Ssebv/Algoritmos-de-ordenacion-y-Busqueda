import random
import time
import matplotlib.pyplot as plt

#Funcion que ordena lista con algoritmo insertion
def ordenar_insercion(lista):
    n = len(lista)
    for j in range(0, n):
        aux = lista[j]
        i = j-1
        while i>-1 and lista[i]>aux:
            lista[i+1] = lista[i]
            i -= 1
        lista[i+1] = aux

#Tamaño inicial del problema
N = 10
tiempo = []
lista_ = []

for i in range(0,12):
    
    lista = [random.randint(0, 50) for iter in range(N)]
    ini = time.time()
    lista_ordenada = ordenar_insercion(lista)
    fin = time.time()
    tiempo.append(fin-ini)
    lista_.append(N)
    
    N = N*2

plt.plot(tiempo, lista_, 'ro')
plt.axis([0,max(tiempo) + 2,0,max(lista_) + 10000])
plt.xlabel('Tiempo')
plt.ylabel('Tamaño de la muestra')
plt.title('Tiempo de busqueda insercion')
plt.show()

