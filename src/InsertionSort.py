#!/usr/bin/python

def insertionSort(tab):
    for i in range(1, len(tab), 1):
        j = i
        while j > 0:
            if tab[j] >= tab[j - 1]:
                tab[j], tab[j - 1] = tab[j - 1], tab[j]
                j -= 1
            else:
                break
    return tab