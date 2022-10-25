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
    answer: dict[str, int] = {}
    color_result: str = ""
    max: int = 0
    for keys in input:
        if input[keys] in answer:
            answer[input[keys]] += 1
        else:
            answer[input[keys]] = 1
    for keys in answer:
        if answer[keys] > max:
            max = answer[keys]
            color_result = keys
    return color_result
    

def count(list1: list[str]) -> dict[str, int]:
    """Will count how many times the value appeared."""
    dict1: dict[str, int] = {}
    i: int = 0
    while i < len(list1):
        if list1[i] in dict1:
            dict1[list1[i]] += 1
        else:
            dict1[list1[i]] = 1
        i += 1
    return dict1