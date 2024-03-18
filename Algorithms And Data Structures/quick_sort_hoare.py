"""
Author:     Chan Guan Yu
Algorithm:  Sorting
Name:       Quick Sort (Hoare)
Stability:  Unstable
"""


def partition(input_list, low, high):
    pivot = input_list[low]
    i = low + 1
    j = high

    while True:
        while i <= j and input_list[i] <= pivot:
            i = i + 1

        while i <= j and input_list[j] > pivot:
            j = j - 1

        if i > j:
            break

        input_list[i], input_list[j] = input_list[j], input_list[i]
    input_list[low], input_list[j] = input_list[j], input_list[low]

    return j


def quick_sort(input_list, low, high):
    if low < high:
        mid = partition(input_list, low, high)
        quick_sort(input_list, low, mid - 1)
        quick_sort(input_list, mid + 1, high)

    return input_list
