"""Code Writing Practice on 10/6/22."""


def zip(list1: list[str], list2: list[str]) -> dict[str, str]:
    """Produces a dictionary where the keys=items of the first list and vales=corresponding items @ same index on second list. """
    assert len(list1) == len(list2)
    result: dict[str, str] = {}
    for i in range(0, len(list1)):
        result[list1[i]] = list2[i]
    return result