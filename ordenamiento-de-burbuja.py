import random
import time
import matplotlib.pyplot as plt


#Funcion que ordena lista con algoritmo burbuja
def ordenar_burbuja(lista):
    n = len(lista)
    for i in range(0, n-1):
        for j in range(i, n):
            if lista[i]>lista[j]:
                lista[i], lista[j] = lista[j], lista[i]
       
#Tamaño inicial del problema                     
N = 10
tiempo = []
lista_ = []

for i in range(0,12):
    
    lista = [random.randint(0, 50) for iter in range(N)]
    #buscamos un elemento que no existe en la lista
    ini = time.time()
    lista_ordenada = ordenar_burbuja(lista)
    fin = time.time()
    tiempo.append(fin-ini)
    lista_.append(N)
    
    N = N*2

plt.plot(tiempo, lista_, 'ro')
plt.axis([0,max(tiempo) + 2,0,max(lista_) + 10000])
plt.xlabel('Tiempo')
plt.ylabel('Tamaño de la muestra')
plt.title('Tiempo del Algoritmo de ordenamiento burbuja')
plt.show()

