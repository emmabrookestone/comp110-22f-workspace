"""EX07-Dictionary Functions."""

__author__ = "730544721"


import pytest
from dictionary import invert, favorite_color, count


def test_invert() -> None:
    """Will flop/invert the keys and values inputs."""
    assert invert({'a': 'z', 'b': 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert1() -> None:
    """Will flop/invert the keys and values inputs."""
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_invert2() -> None:
    """Will flop/invert the keys and values inputs."""
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_favorite_color() -> None: 
    """Will return the color that is most frequent."""
    assert favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == "blue"


def test_favorite_color1() -> None:
    """Will return the color that is most frequent."""
    assert favorite_color({"Emma": "blue", "Jua": "yellow", "Sarah": "pink", "Zach": "orange", "Cam": "pink"}) == "pink"


def test_favorite_color2() -> None:
    """Will return the color that is most frequent."""
    favorite_color_test: dict[str, str] = {"Rice": "red", "Stewart": "red", "Stone": "red", "Kelly": "red"}
    assert favorite_color(favorite_color_test) == "red"


def test_count() -> None:
    """Will count how many times the value appeared."""
    assert count(['0', '1', '2']) == ({'0': 1, '1': 1, '2': 1})


def test_count1() -> None:
    """Will count how many times the value appeared."""
    assert count(['100', '200', '200']) == ({'100': 1, '200': 2})


def test_count2() -> None:
    """Will count how many times the value appeared."""
    assert count(['Cam', 'Zach', 'Anna', 'Eli']) == ({'Cam': 1, 'Zach': 1, 'Anna': 1, 'Eli': 1})