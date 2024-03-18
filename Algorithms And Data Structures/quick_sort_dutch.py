"""
Author:     Chan Guan Yu
Algorithm:  Sorting
Name:       Quick Sort (Dutch National Flag)
Stability:  Unstable
"""


def partition(input_list, low, high):
    pivot = input_list[low]
    j = low + 1

    while j <= high:
        if input_list[j] < pivot:
            input_list[j], input_list[low] = input_list[low], input_list[j]
            low = low + 1
            j = j + 1
        elif input_list[j] == pivot:
            j = j + 1
        else:
            input_list[j], input_list[high] = input_list[high], input_list[j]
            high = high - 1

    return low, high


def quick_sort(input_list, low, high):
    if low < high:
        boundary1, boundary2 = partition(input_list, low, high)
        quick_sort(input_list, low, boundary1 - 1)
        quick_sort(input_list, boundary2 + 1, high)

    return input_list
