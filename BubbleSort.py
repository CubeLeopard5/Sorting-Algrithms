#!/usr/bin/python

def bubbleSort(tab):
    for i in range(len(tab) - 1):
        for j in range(0, len(tab) - i - 1):
            if tab[j] > tab[j + 1] :
                tab[j], tab[j + 1] = tab[j + 1], tab[j]
    return tab