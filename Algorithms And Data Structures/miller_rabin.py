"""
Author:     Chan Guan Yu
Algorithm:  Numerical
Name:       Miller-Rabin Primality Test
"""


import random


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
