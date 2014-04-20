# -*- coding: utf-8 -*-

from time import time

def insertionSort(lista):
    n = len(lista)
    global ciclos

    for i in range(1, n):
        val = lista[i]
        j = i

        while j > 0 and lista[j - 1] > val:
            lista[j] = lista[j-1]
            j -= 1
            ciclos += 1

        lista[j] = val


lista = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]
ciclos = 0

t0 = time()
ciclos = insertionSort(lista)
t1 = time()

print "Lista ordenada:"
print lista, "\n"

print "Tiempo: {0:f} segundos".format(t1 - t0)
print "Ciclos:", ciclos