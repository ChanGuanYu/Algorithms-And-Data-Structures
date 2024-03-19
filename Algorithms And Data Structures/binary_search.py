"""
Author:     Chan Guan Yu
Algorithm:  Search
Name:       Binary Search
"""


def binary_search(search_list, target):
    n = len(search_list)
    low = 0
    high = n - 1

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


def binary_search_recursive(search_list, target, low, high):
    if low <= high:
        mid = low + (high - low) // 2
        mid_val = search_list[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
            return binary_search_recursive(search_list, target, low, high)
        else:
            high = mid - 1
            return binary_search_recursive(search_list, target, low, high)
    else:
        return -1
