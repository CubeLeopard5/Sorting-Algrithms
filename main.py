#!/usr/bin/python3

from src.SelectionSort import selectionSort
from src.InsertionSort import insertionSort
from src.QuickSort import quickSort
from src.MergeSort import mergeSort
from src.ShellSort import shellSort
from src.BubbleSort import bubbleSort
import copy
import time

def execSort(userInput, tab):
    res = []
    start_time = time.time()
    if (userInput[0]  == "SelectionSort"):
        res = selectionSort(copy.deepcopy(tab))
    elif (userInput[0] == "BubbleSort"):
        res = bubbleSort(copy.deepcopy(tab))
    elif (userInput[0] == "InsertionSort"):
        res = insertionSort(copy.deepcopy(tab))
    elif (userInput[0] == "QuickSort"):
        res = quickSort(copy.deepcopy(tab))
    elif (userInput[0] == "MergeSort"):
        res = mergeSort(copy.deepcopy(tab))
    elif (userInput[0] == "ShellSort"):
        res = shellSort(len(tab), copy.deepcopy(tab))
    print("The array {} has been sort = {}. Time = ".format(tab, res), end="")
    print(time.time() - start_time, end=" ")
    print("seconds")
    return res

def getInput():
    while True:
        userInput = input()
        if (userInput == "END"):
            break
        userInput = userInput.split(' ')
        try:
            tab = userInput[1].split(",")
            for i in range(len(tab)):
                tab[i] = int(tab[i])
        except Exception as ex:
            print(f"ERROR message - unsupported size or other error: {ex}")
            return(84)
        execSort(userInput, tab)
    return 0

if __name__ == '__main__':
    print("Commands: write the name of the sort algorithm (SelectionSort, BubbleSort, InsertionSort, MergeSort, QuickSort, ShellSort)")
    print("followed by the list of numbers")
    print("Example: SelectionSort 3,43,0,-6,13,1")
    getInput()