#!/usr/bin/python

def partition(tab):
    l = []
    r = []
    for i in range(1, len(tab), 1):
        l.append(tab[i]) if tab[i] >= tab[0] else r.append(tab[i])
    return tab, l, r

def quickSort(tab):
    if len(tab) <= 1:
        return tab
    tab, left, right = partition(tab)
    sortLeft = quickSort(left)
    sortRight = quickSort(right)
    tab = sortLeft[0] + [tab[0]] + sortRight[0]
    return tab