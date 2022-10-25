"""Functions skeletons and implementations are here."""


__author__ = "730544721"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Will flop/invert the keys and values inputs."""
    result: dict[str, str] = {}
    for x in input:
        if input[x] in result:
            raise KeyError
        result[input[x]] = x
    return result


def favorite_color(input: dict[str, str]) -> str:
    """Will return the color that is most frequent."""
    result: str = {}
    i: int = 0
    x: str = input[i]
    while i < len(input):
        if x == favorite_color[i]:
            return result
        else:
            i += 1


def count(list1: list[str]) -> dict[str, int]:
    """Will count how many times the value appeared."""
    result: int = {}
    i: int = 0
    while i < len(input):
        if list1[i] in result:
            result[list1[i]] += 1
        else:
            result[list1[i]] == 1
    return result