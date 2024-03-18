"""
Author:     Chan Guan Yu
Algorithm:  Numerical
Name:       Twin Prime Generator
"""


import sys
import random
import math


def mod_exp(base, exp, mod):
    """
    A function that performs pow(base, exp, mod)
    Uses repeated squaring method
    Arguments:
        base: An integer which is the base/dividend
        exp: An integer which is the exponent
        mod: An integer which is the divisor
    Time complexity:
        O(log(n)), by dividing exponent by 2, we would require log(n)
        divisions (ignoring the constants), where logarithm base
        is 2, n is the exponent.
    Space complexity:
        O(p), where p is the number of bits, exponent has. When checking
        if binary representation of exponent has 1 at position i, a temporary
        binary number is created with 1 at position i, with at most length p.
    Return: An integer which is the result of (base ** exp) % mod
    """

    # The original exponent value
    og_exp = exp

    result = 1
    i = 0
    while exp > 0:

        # If binary representation of exponent has 1 at position i
        # Original exponent in binary is checked with binary number with 1 at position i
        # If condition is true, update result
        if og_exp & (1 << i):
            result = (result * base) % mod

        # Divide exponent by 2
        exp = exp // 2

        # Apply key property
        # x * y mod z = (x mod z * y mod z) mod z
        base = (base * base) % mod
        i = i + 1

    return result


def miller_rabin(n, k=64):
    """
    A function that tests whether a number is prime or composite
    The number of witnesses used varies depending on the number
    Arguments:
        n: An integer to be tested
        k: An integer which is the number of witnesses
    Time complexity:
        O(k(log(n))), the main loop runs k times, and for each loop,
        mod_exp() is called 3 times, so total would be (ignoring constants)
        = O(k * (log(n) + log(n) + log(n))) = O(k(log(n))).
    Space complexity:
        O(p), for every mod_exp() call, a temporary binary number with
        at most length p is created.
    Return: A Boolean value, if n is probably prime, return True, else
            return False
    """

    # If n is even, it is definitely composite, return False
    if n % 2 == 0:
        return False

    # Factor n - 1 as (2 ** s) * t, where t is odd
    s = 0
    t = n - 1
    while t % 2 == 0:
        s = s + 1
        t = t//2

    for x in range(k):

        # Choose random number in the range 1 < a < n - 1
        a = random.randrange(2, n - 1)

        if mod_exp(a, n - 1, n) != 1:
            return False

        # Loop from i = 1
        # Create variables (curr_i & prev_i) to remember the initial values
        # Then slowly build up the values
        i = 1
        curr_i = mod_exp(a, 2 * t, n)
        prev_i = mod_exp(a, 1 * t, n)

        while i <= s:

            if (curr_i == 1) and (prev_i != 1) and (prev_i != n - 1):
                return False

            i = i + 1
            prev_i = curr_i
            curr_i = (curr_i * curr_i) % n

    return True


def select_k(n):
    """
    A function that determines the number of witnesses based on n
    log(n) witnesses are required, but if log(n) is smaller than 64,
    64 is used
    Arguments:
        n: An integer
    Time complexity:
        O(1)
    Space complexity:
        O(1)
    Return: An integer k, where k is the number of witnesses
    """

    # k is at least 64
    k = 64
    if math.log(n) > k:
        k = math.ceil(math.log(n))

    return k


def twin_prime_generator(m):
    """
    A function that finds a twin prime pair
    Uses Miller-Rabin's Randomized Primality Testing Algorithm
    Arguments:
        m: An integer, representing the number of bits
    Time complexity:
        O(k(log**3(n)), in best case, miller_rabin() is called twice,
        while in worst case, miller_rabin() is called three times.
        Because n + 2 is checked first, and if n + 2 is not prime, n - 2
        must be checked. Ignoring constants, we get O(k(log**3(n))).
    Space complexity:
        O(p), the space complexity of miller_rabin() is at most O(p),
        regardless if it is called 2 or 3 times, as constants are ignored.
        So, the constant space of the list storing the twin prime pair is
        also ignored.
    Return: N/A
    """

    twin_prime_pair = []
    found = False
    while found is False:

        # Random number n in [2**(m - 1), 2**m - 1]
        n = random.randrange(2 ** (m - 1), 2 ** m)

        # Select k, where k is at least 64
        # Based on n
        k = select_k(n)

        is_prime = miller_rabin(n, k)

        if is_prime is True:

            # Check for n + 2 first
            larger_prime = miller_rabin(n + 2, select_k(n + 2))
            if larger_prime is True:
                twin_prime_pair.append(n)
                twin_prime_pair.append(n + 2)
                break

            # If n + 2 is not prime, check n - 2
            smaller_prime = miller_rabin(n - 2, select_k(n - 2))
            if smaller_prime is True:
                twin_prime_pair.append(n - 2)
                twin_prime_pair.append(n)
                break

            if (larger_prime is False) and (smaller_prime is False):
                continue
        else:
            continue

    output(twin_prime_pair)


def output(pair):
    """
    A function that writes the output in a text file
    Arguments:
        pair: A list storing 2 values, a pair of twin primes
    Time complexity:
        O(1)
    Space complexity:
        O(1)
    Return: N/A
    """

    newline = "\n"
    with open("output_twin_prime.txt", "w") as file:
        # Output smaller prime then larger prime
        file.write(str(pair[0]) + newline + str(pair[1]))
    file.close()


if __name__ == "__main__":
    # Store argument in variable
    m = int(sys.argv[1])

    # Find the twin prime pair
    twin_prime_generator(m)
