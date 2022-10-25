"""EX04 'List' Utility Functions."""


__author__ = "730544721"


def all(multiple: list[int], single: int) -> bool:
    """Will return True if all number match single but return False otherwise or if list is empty."""
    i: int = 0
    if len(multiple) == 0:
        return False
    while i < len(multiple):
        if multiple[i] != single:
            return False
        i += 1
    return True


def max(input: list[int]) -> int:
    """Will find max number in list."""
    m: int = input[0]
    i: int = 1
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    while i < len(input):
        if input[i] > m:
            m = input[i]
        i += 1
    return m


def is_equal(first: list[int], second: list[int]) -> bool:
    """Will return True is every element at every index is equal in both lists."""
    if first == second:
        return True
    else: 
        return False