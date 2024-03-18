"""
Author:     Chan Guan Yu
Algorithm:  Sorting
Name:       Merge Sort
Stability:  Stable
"""


def merge(left, right):
    merged_list = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged_list.append(left[i])
            i = i + 1
        else:
            merged_list.append(right[j])
            j = j + 1

    while i < len(left):
        merged_list.append(left[i])
        i = i + 1

    while j < len(right):
        merged_list.append(right[j])
        j = j + 1

    return merged_list


def merge_sort(input_list):
    n = len(input_list)

    if n > 1:
        mid = n // 2
        left = merge_sort(input_list[:mid])
        right = merge_sort(input_list[mid:])
        output_list = merge(left, right)
        return output_list
    else:
        return input_list
