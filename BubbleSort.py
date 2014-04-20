# -*- coding: utf-8 -*-

from time import time

def bubbleSort(lista):
    global ciclos
    n = len(lista)

    for i in range(1,n-1):
        for j in range(n-i):
            ciclos += 1
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

lista = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
ciclos = 0

t0 = time()
bubbleSort(lista)
t1 = time()

print "Lista ordenada:"
print lista, "\n"

print "Tiempo: {0:f} segundos".format(t1 - t0)
print "Ciclos:", ciclos
