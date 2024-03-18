"""
Author:     Chan Guan Yu
Algorithm:  Sorting
Name:       Counting Sort
Stability:  Stable
"""


def counting_sort(input_list):
    n = len(input_list)
    max_val = max(input_list)
    min_val = min(input_list)

    k = max_val - min_val + 1

    count_arr = [0] * k
    output_arr = [0] * n

    for i in range(n):
        val = input_list[i] - min_val
        count_arr[val] = count_arr[val] + 1

    for i in range(1, k):
        count_arr[i] = count_arr[i] + count_arr[i - 1]

    for i in range(n - 1, -1, -1):
        val = input_list[i] - min_val
        output_arr[count_arr[val] - 1] = input_list[i]
        count_arr[val] = count_arr[val] - 1

    return output_arr
