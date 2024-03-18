"""
Author:     Chan Guan Yu
Algorithm:  Compression
Name:       Elias Omega Coding
"""


from collections import deque


def to_binary(num, encoded_num):
    """
    A function that converts a decimal number to a binary number
    Works with elias_encode() to perform encoding
    Arguments:
        num: A decimal number
        encoded_num: A deque
    Time complexity:
        O(log(n)), as we are dividing the number by 2. This is also
        the number of bits required to represent the number in binary.
    Space complexity:
        O(log(n)), every time the number is divided by 2, a character
        of "0" or "1" is appended, so at most there will be log(n)
        characters appended.
    Return: A tuple of deque and length of minimal binary code of number
    """

    # Length of minimal binary code of number
    length = 0

    while num > 0:
        if num % 2 == 0:
            encoded_num.appendleft("0")
            length = length + 1
        else:
            encoded_num.appendleft("1")
            length = length + 1
        num = num // 2

    return encoded_num, length


def elias_omega_encode(num):
    """
    A function that performs Elias Omega encoding
    Arguments:
        num: An integer to be encoded
    Time complexity:
        O(log(n)), which is the number of bits required to
        represent the number n in binary.
    Space complexity:
        O(n)
    Return: A string of bits, which is the code word for input num
    """

    encoded_num = deque([])

    # Only works if num is at least 1
    if num != 0:

        # Code component
        encoded_num, num_length = to_binary(num, encoded_num)

        num_length = num_length - 1

        # Length components
        while num_length >= 1:

            # Repeat the same process as above
            encoded_num, num_length = to_binary(num_length, encoded_num)

            # Change the leading 1 of its minimal binary code to 0
            encoded_num.popleft()
            encoded_num.appendleft("0")

            num_length = num_length - 1

    # Join everything in the deque to produce a bitstring
    encoded_num = "".join(encoded_num)

    return encoded_num
