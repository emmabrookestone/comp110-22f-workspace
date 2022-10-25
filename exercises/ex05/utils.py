"""Functions skeletons and implementations are here."""

__author__ = "730544721"


def only_evens(input: list[int]) -> list[int]:
    """Will return the even numbers within the list."""
    result: list[int] = list()
    i: int = 0
    while i < len(input):
        if input[i] % 2 == 0:
            result.append(input[i])
        i += 1
    return result


def concat(input1: list[int], input2: list[int]) -> list[int]:
    """Will return input1 followed by input2 without mutating either of the arguments."""
    outcome: list[int] = list()
    i: int = 0
    while i < len(input1):
        outcome.append(input1[i])
        i += 1
    i = 0
    while i < len(input2): 
        outcome.append(input2[i])
        i += 1
    return outcome


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Will return a list but is in between the s†art and end index - 1."""
    result: list[int] = list()
    i: int = start
    m: int = end
    if start < 0:
        i = 0
    if end > len(input):
        m = len(input)
    while i < m:
        result.append(input[i])
        i += 1
    return result