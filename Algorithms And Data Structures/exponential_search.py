"""
Author:     Chan Guan Yu
Algorithm:  Search
Name:       Exponential Search
"""


def binary_search(search_list, target, low, high):
    while low <= high:
        mid = low + (high - low) // 2
        mid_val = search_list[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def exponential_search(search_list, target):
    n = len(search_list)

    if search_list[0] == target:
        return 0

    i = 1
    while i < n and search_list[i] <= target:
        i = i * 2

    low = i // 2
    high = min(i, n - 1)
    return binary_search(search_list, target, low, high)
