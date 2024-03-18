"""
Author:     Chan Guan Yu
Algorithm:  Sorting
Name:       Radix Sort
Stability:  Stable
"""


def counting_sort(input_list, col, base):
    n = len(input_list)
    count_arr = [0] * base
    output_arr = [0] * n

    for val in input_list:
        index = (val // (base ** col)) % base
        count_arr[index] = count_arr[index] + 1

    for i in range(1, base):
        count_arr[i] = count_arr[i] + count_arr[i - 1]

    for i in range(n - 1, -1, -1):
        val = input_list[i]
        index = (val // (base ** col)) % base
        output_arr[count_arr[index] - 1] = val
        count_arr[index] = count_arr[index] - 1

    return output_arr


def radix_sort(input_list, base):
    n = len(input_list)
    max_val = max(input_list)
    min_val = min(input_list)

    digits = 0
    while max_val > 0:
        max_val = max_val // base
        digits = digits + 1

    output_list = []
    for val in input_list:
        output_list.append(val)

    has_negative = False
    if min_val < 0:
        has_negative = True
        for i in range(n):
            output_list[i] = output_list[i] - min_val

    for col in range(digits):
        output_list = counting_sort(output_list, col, base)

    if has_negative:
        for i in range(n):
            output_list[i] = output_list[i] + min_val

    return output_list
