"""
Author:     Chan Guan Yu
Algorithm:  Compression
Name:       Huffman and Elias Omega Header Constructor
"""


import sys
import heapq
from collections import deque


class Node:
    """
    A class which represents a node in a heap
    """

    def __init__(self, char, freq):
        """
        Initialization of instance variables
        """

        self.char = char
        self.freq = freq

    def __lt__(self, other):
        """
        A magic method, by overriding it, it can be used to overload the "less than" operator
        Allows Node objects to be compared using freq and len(char)
        """

        return (self.freq < other.freq) or ((self.freq == other.freq) and (len(self.char) < len(other.char)))

    def __str__(self):
        """
        A magic method, by overriding it, allows a printable string representation to be returned
        """

        return "Character: " + self.char + ", Frequency: " + str(self.freq)


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


def to_ascii(num):
    """
    A function that converts a decimal number to a binary number
    If the number does not reach a length of 7 bits, add leading
    zeroes
    Arguments:
        num: A decimal number
    Time complexity:
        O(log(n)), as we are dividing the number by 2. This is also
        the number of bits required to represent the number in binary.
        Joining the deque elements also take O(log(n)), but since
        constants are ignored, complexity is still O(log(n)).
    Space complexity:
        O(log(n)), every time the number is divided by 2, a character
        of "0" or "1" is appended, so at most there will be log(n)
        characters appended.
    Return: A string of binary number with a length of 7 bits
    """

    result = deque([])
    while num > 0:
        if num % 2 == 0:
            result.appendleft("0")
        else:
            result.appendleft("1")
        num = num // 2

    # Add leading zeroes, to ensure the length is 7
    if len(result) < 7:
        while len(result) < 7:
            result.appendleft("0")

    result = "".join(result)
    return result


def huffman_encode(string):
    """
    A function that performs Huffman coding
    Uses heapq and its operations
    Arguments:
        string: A string to be encoded
    Time complexity:
        O(n*log(n)), where n is the number of unique characters in the string.
        In the worst case, n equals to the length of the string. In the main
        while loop, heapq's heappop() is called twice for each iteration,
        which is 2 * (O(log(n)). Multiplying it together, we get O(n*log(n)).
    Space complexity:
        O(n), where n is the number of unique characters in the string. It should
        be O(128) + O(128) + O(n), which are freq_arr, code_word_arr and code_words.
        But since constants are ignored, we can say that it is O(n).
    Return: A list of tuples (character, code word)
    """

    freq_arr = [0] * 128
    code_word_arr = [None] * 128
    heap = []

    # Obtain each character's frequency/probability
    for char in string:
        freq_arr[ord(char)] = freq_arr[ord(char)] + 1

    # Create heap, insert nodes and heapify heap
    for i in range(len(freq_arr)):
        if freq_arr[i] != 0:
            char = chr(i)
            freq = freq_arr[i]
            heap.append(Node(char, freq))
    heapq.heapify(heap)

    # If there is only one character
    # Give it the code word "0" and return
    if len(heap) == 1:
        char = heap[0].char
        code_word_arr[ord(char)] = "0"
        return

    # Main algorithm
    # Replace none with deque
    # Deque allows prepend to have constant time complexity, using appendleft()
    while len(heap) > 1:
        node_1 = heapq.heappop(heap)
        node_2 = heapq.heappop(heap)

        # In the first "serve", give the characters the code letter "0"
        for c in node_1.char:

            # If it is already a deque, just prepend
            if code_word_arr[ord(c)] is not None:
                code_word_arr[ord(c)].appendleft("0")
            else:
                code_word_arr[ord(c)] = deque([])
                code_word_arr[ord(c)].appendleft("0")

        # In the second "serve", give the characters the code letter "1"
        for c in node_2.char:

            # If it is already a deque, just prepend
            if code_word_arr[ord(c)] is not None:
                code_word_arr[ord(c)].appendleft("1")
            else:
                code_word_arr[ord(c)] = deque([])
                code_word_arr[ord(c)].appendleft("1")

        # Create a new node, with the combined character and frequency
        # Put it back into the heap
        new_char = node_1.char + node_2.char
        new_freq = node_1.freq + node_2.freq
        new_node = Node(new_char, new_freq)
        heapq.heappush(heap, new_node)

    # After generating the code words for all characters
    # Create a list of tuples (character, code word) as output
    code_words = []
    for c in range(len(code_word_arr)):
        if code_word_arr[c] is not None:
            code_word_arr[c] = "".join(code_word_arr[c])
            code_words.append((chr(c), code_word_arr[c]))

    return code_words


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


def header_constructor(string):
    """
    A function that constructs a header that contains all the information
    necessary to decode an input string
    Uses Huffman and Elias Omega coding
    Arguments:
        string: A string
    Time complexity:
        O(n*log(n)), as this function uses Huffman and Elias Omega coding,
        it is bounded by the time complexity of Huffman coding.
    Space complexity:
        O(n**2), in the worst case, the number of unique characters is equal
        to the string length. Knowing that the largest component of a header
        is the 7-bit ASCII value of the characters, the header output is at
        least 7 * n in length. Therefore, the upper bound should be O(n**2).
    Return: N/A
    """

    result = deque([])
    code_words = huffman_encode(string)

    # Append the number of unique ASCII characters
    unique_chars = elias_omega_encode(len(code_words))
    result.append(unique_chars)

    # For each unique character in the string
    for c in range(len(code_words)):

        # Unique character in 7-bit ASCII value
        c_ascii = to_ascii(ord(code_words[c][0]))
        result.append(c_ascii)

        # Length of the Huffman code assigned to the unique character
        code_length = elias_omega_encode(len(code_words[c][1]))
        result.append(code_length)

        # Variable-length Huffman code word assigned to the unique character
        result.append(code_words[c][1])

    result = "".join(result)
    output(result)
    return result


def output(result):
    """
    A function that writes the output in a text file
    Arguments:
        result: A string of bits
    Time complexity:
        O(1)
    Space complexity:
        O(1)
    Return: N/A
    """

    with open("output_header.txt", "w") as file:
        file.write(str(result))
    file.close()


if __name__ == "__main__":
    # Store argument in variable
    text_file = sys.argv[1]

    # Construct header
    string = open(text_file, "r").readline()
    header_constructor(string)
