"""
Author:     Chan Guan Yu
Algorithm:  Compression
Name:       Huffman Coding
"""


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
