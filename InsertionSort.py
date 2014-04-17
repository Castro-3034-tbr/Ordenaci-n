# -*- coding: utf-8 -*-

from time import time

def insertionSort(lista):
    n = len(lista)
    ciclos = 0

    for i in range(1, n):
        j = i

        while j > 0 and lista[j] < lista[j - 1]:
            ciclos += 1
            lista[j], lista[j-1] = lista[j-1], lista[j]
            j -= 1

    return lista, ciclos


lista = [36, 71, 16, 21, 73, 9, 0, 40, 66, 5]

print "Lista de números desordenados:"
print lista, "\n"

t0 = time()
lista, ciclos = insertionSort(lista)
t1 = time()

print "Lista de números ordenados:"
print lista, "\n"

print "Tiempo: {0:f} segundos".format(t1 - t0)
print "Ciclos:", ciclos