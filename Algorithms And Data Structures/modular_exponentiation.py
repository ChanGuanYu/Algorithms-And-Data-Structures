"""
Author:     Chan Guan Yu
Algorithm:  Numerical
Name:       Modular Exponentiation
"""


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
