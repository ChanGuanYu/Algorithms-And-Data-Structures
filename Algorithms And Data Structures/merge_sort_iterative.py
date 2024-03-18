"""
Author:     Chan Guan Yu
Algorithm:  Sorting
Name:       Merge Sort (Iterative)
Stability:  Stable
"""


def merge(input_list, temp_list, start, mid, end):
    i, k = start, start
    j = mid + 1

    while i <= mid and j <= end:
        if input_list[i] <= input_list[j]:
            temp_list[k] = input_list[i]
            i = i + 1
        else:
            temp_list[k] = input_list[j]
            j = j + 1
        k = k + 1

    while i <= mid:
        temp_list[k] = input_list[i]
        i = i + 1
        k = k + 1

    while j <= end:
        temp_list[k] = input_list[j]
        j = j + 1
        k = k + 1

    for i in range(start, end + 1):
        input_list[i] = temp_list[i]


def merge_sort(input_list):
    n = len(input_list)
    last_index = n - 1
    temp_list = [0] * n

    if n <= 1:
        return input_list

    size = 1
    while size < n:
        start = 0
        while start < n:
            left_end = start + size - 1
            mid = min(left_end, last_index)

            right_end = mid + size
            end = min(right_end, last_index)

            merge(input_list, temp_list, start, mid, end)
            start = start + size * 2
        size = size * 2

    return input_list
