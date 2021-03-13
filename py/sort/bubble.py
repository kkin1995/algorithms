import numpy as np
import matplotlib.pyplot as plt

def bubble_sort(array):
    swap_has_occured = True
    while swap_has_occured:
        swap_has_occured = False
        for i in range(1, len(array)):
            if array[i-1] > array[i]:
                array[i-1], array[i] = array[i], array[i-1]
                swap_has_occured = True
    return array

if __name__ == '__main__':
    array = [83,49,4873,9843,5,942]
    print("Unsorted Array = ", array)
    print("Sorted Array = ", bubble_sort(array))