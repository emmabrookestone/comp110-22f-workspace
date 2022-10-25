"""'List' Utility Functions Test."""

__author__ = "730544721"


from exercises.ex05.utils import concat, only_evens, sub


def test_only_evens() -> None:
    """Will return the even numbers within the list."""
    assert only_evens([1, 2, 3]) == [2]


def test_only_evens_1() -> None:
    """Will return the even numbers within the list."""
    assert only_evens([2, 4, 9]) == [2, 4]


def test_only_evens_2() -> None:
    """Will return the even numbers within the list."""
    assert only_evens([1, 7, 3]) == []


def test_concat() -> None:
    """Will return input1 followed by input2 without mutating either of the arguments."""
    assert concat([1, 2, 10, 4], [12, 1, 19, 4]) == [1, 2, 10, 4, 12, 1, 19, 4]


def test_concat_2() -> None:
    """Will return input1 followed by input2 without mutating either of the arguments."""
    assert concat([2, 4, 6, 4], [1, 10, 21, 40]) == [2, 4, 6, 4, 1, 10, 21, 40]


def test_concat_3() -> None:
    """Will return input1 followed by input2 without mutating either of the arguments."""
    assert concat([10, 20, 30, 40], [5, 10, 15, 20]) == [10, 20, 30, 40, 5, 10, 15, 20]


def test_sub() -> None:
    """Will return a list but is in between the s†art and end index - 1."""
    a_list: list[int] = [10, 20, 30, 40]
    assert sub(a_list, 1, 3) == [20, 30]


def test_sub_2() -> None:
    """Will return a list but is in between the s†art and end index - 1."""
    a_list: list[int] = [1, 4, 6, 9]
    assert sub(a_list, 1, 2) == [4]


def test_sub_3() -> None:
    """Will return a list but is in between the s†art and end index - 1."""
    a_list: list[int] = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
    assert sub(a_list, 4, 8) == [10, 12, 14, 16]