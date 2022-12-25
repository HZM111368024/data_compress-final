"""Module providing didactical tools to show encoding and decoding of the Golomb format"""

from math import ceil, log2
from typing import List


def golomb_coding(n: int, m: int) -> str:
    """Return string representing given number in golomb coding.
    Parameters
    ------------------------
    n: int
        Number to convert to golomb coding.
    b: int
        Module.
    """
    #print("n and m : " + str(n) + "  " + str(m))
    return inverted_unary(n // (m ** 2)) + minimal_binary_coding(n % int((m ** 2)), int(m ** 2))


def golomb_decoding(golomb_code: str, b: int) -> str:
    """Return integer represented in provided golomb code.
    Parameters
    ------------------------
    golomb_code: str
        Golomb encoding to be converted back.
    b: int
        Module.
    """
    inverted_unary_portion_len = get_len_of_leading_inverted_unary(golomb_code)
    decoded_inverted_unary_portion = decode_leading_inverted_unary(golomb_code)
    decoded_minimal_binary = decode_minimal_binary(
        golomb_code[inverted_unary_portion_len:],
        b
    )
    return decoded_inverted_unary_portion * b + decoded_minimal_binary


def best_golomb_coding(numbers: List[int]) -> List[str]:
    """Return list of strings representing given numbers in bernoulli golomb coding.
    Parameters
    ------------------------
    numbers: List[int]
        List of numbers to convert to bernoulli golomb coding.
    """
    frequencies = {}
    N = len(numbers)
    for n in numbers:
        frequencies[n] = frequencies.get(n, 0) + 1

    k = 0
    for n in numbers:
        #print(frequencies[n] / N, n)
        if frequencies[n] / N == 1 and (n == 0 or n == 1):
            k = 1
        elif frequencies[n] / N == 1:
            k = frequencies[n] / N * ceil(log2(n))
            break
        else:
            k += frequencies[n] / N * ceil(log2(n))

    return [
        golomb_coding(n, k)
        for n in numbers
    ]


def get_maximal_code_length(b: int) -> int:
    """Return the maximal length of the code."""
    return ceil(log2(b))


def minimal_binary_coding(n: int, b: int) -> str:
    """Return string representing given number in minimal binary coding.

    Parameters
    -------------------------
    n: int
        Number to convert to minimal binary encoding.
    b: int
        Maximal size.
    """
    if n == 0 and b == 1:
        return "0"
    code_maximal_len = get_maximal_code_length(b)
    if n < 2 ** code_maximal_len - b:
        return f"{{0:0{code_maximal_len - 1}b}}".format(n)
    return f"{{0:0{code_maximal_len}b}}".format(n - b + 2 ** code_maximal_len)


def decode_minimal_binary(minimal_binary_code: str, b: int) -> int:
    """Return integer obtained decoding provided minimal binary string.

    Parameters
    -------------------------
    minimal_binary_code: str
        The minimal binary code to convert back to integer
    b: int
        Maximal size.
    """
    code_maximal_len = get_maximal_code_length(b)

    if len(minimal_binary_code) != code_maximal_len:
        return int(minimal_binary_code, 2)

    return int(minimal_binary_code, 2) + b - 2 ** code_maximal_len


def _unary(n: int, zero: str, one: str) -> str:
    return one * int(n) + zero


def inverted_unary(n: int) -> str:
    """Return string representing given number in inverted unary.
        n:int, number to convert to unary.
    """
    return _unary(n, "0", "1")


def get_len_of_leading_inverted_unary(string_starting_with_inverted_unary: str) -> int:
    """Returns length of leading inverted unary portion in string."""
    return decode_leading_inverted_unary(string_starting_with_inverted_unary) + 1


def decode_leading_inverted_unary(string_starting_with_inverted_unary: str) -> int:
    """Returns decoded unary value."""
    return string_starting_with_inverted_unary.index("1")
