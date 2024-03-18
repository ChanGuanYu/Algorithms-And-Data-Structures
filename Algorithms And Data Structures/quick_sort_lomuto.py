"""
Author:     Chan Guan Yu
Algorithm:  Sorting
Name:       Quick Sort (Lomuto)
Stability:  Unstable
"""


def partition(input_list, low, high):
    pivot = input_list[high]
    i = low - 1

    for j in range(low, high):
        if input_list[j] <= pivot:
            i = i + 1
            input_list[i], input_list[j] = input_list[j], input_list[i]
    input_list[i + 1], input_list[high] = input_list[high], input_list[i + 1]

    return i + 1


def quick_sort(input_list, low, high):
    if low < high:
        mid = partition(input_list, low, high)
        quick_sort(input_list, low, mid - 1)
        quick_sort(input_list, mid + 1, high)

    return input_list
