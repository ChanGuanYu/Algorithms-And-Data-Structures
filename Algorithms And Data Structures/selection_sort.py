"""
Author:     Chan Guan Yu
Algorithm:  Sorting
Name:       Selection Sort
Stability:  Stable
"""


def selection_sort(input_list):
    n = len(input_list)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if input_list[j] < input_list[min_index]:
                min_index = j
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
    return input_list
