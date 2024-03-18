"""
Author:     Chan Guan Yu
Algorithm:  Sorting
Name:       Heap Sort
Stability:  Unstable
"""


def heapify(input_list, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and input_list[left] > input_list[largest]:
        largest = left

    if right < n and input_list[right] > input_list[largest]:
        largest = right

    if largest != i:
        input_list[i], input_list[largest] = input_list[largest], input_list[i]
        heapify(input_list, n, largest)


def heap_sort(input_list):
    n = len(input_list)

    for i in range(n // 2 - 1, -1, -1):
        heapify(input_list, n, i)

    for i in range(n - 1, 0, -1):
        input_list[i], input_list[0] = input_list[0], input_list[i]
        heapify(input_list, i, 0)

    return input_list
