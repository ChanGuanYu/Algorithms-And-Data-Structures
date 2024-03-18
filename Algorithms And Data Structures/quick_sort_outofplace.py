"""
Author:     Chan Guan Yu
Algorithm:  Sorting
Name:       Quick Sort (Out-of-Place)
Stability:  Stable
"""


def partition(input_list):
    n = len(input_list)
    pivot = input_list[0]
    pivots = [pivot]
    left, right = [], []

    for i in range(1, n):
        if input_list[i] < pivot:
            left.append(input_list[i])
        elif input_list[i] == pivot:
            pivots.append(input_list[i])
        else:
            right.append(input_list[i])

    return left, pivots, right


def quick_sort(input_list):
    n = len(input_list)

    if n <= 1:
        return input_list
    else:
        left, pivots, right = partition(input_list)
        return quick_sort(left) + pivots + quick_sort(right)
