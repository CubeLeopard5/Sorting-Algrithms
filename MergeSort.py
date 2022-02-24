#!/usr/bin/python

def mergeSort(tab):
    if len(tab) > 1:
        middle = len(tab) // 2
        left = tab[:middle]
        right = tab[middle:]
        tab = mergeSort(left)
        tab = mergeSort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                tab[k] = left[i]
                i += 1
            else:
                tab[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            tab[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            tab[k] = right[j]
            j += 1
            k += 1
    return tab