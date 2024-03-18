"""
Author:     Chan Guan Yu
Algorithm:  Sorting
Name:       Bubble Sort
Stability:  Stable
"""


def bubble_sort(input_list):
    n = len(input_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if input_list[j] > input_list[j + 1]:
                input_list[j], input_list[j + 1] = input_list[j + 1], input_list[j]
                swapped = True
        if not swapped:
            break
    return input_list
