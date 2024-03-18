"""
Author:     Chan Guan Yu
Algorithm:  Sorting
Name:       Insertion Sort
Stability:  Stable
"""


def insertion_sort(input_list):
    n = len(input_list)
    for i in range(1, n):
        val = input_list[i]
        j = i - 1
        while j >= 0 and val < input_list[j]:
            input_list[j + 1] = input_list[j]
            j = j - 1
        input_list[j + 1] = val
    return input_list
