"""EX07-Dictionary Functions."""

__author__: "730544721"

import pytest
from exercises.ex07.dictionary import invert, favorite_colors, count


def test_invert() -> None:
    assert invert({'a': 'z', 'b' : 'y', 'c': 'x'}) == {'z': 'a', 'y': 'b', 'x': 'c'}


def test_invert1() -> None:
    assert invert({'apple': 'cat'}) == {'cat': 'apple'}


def test_invert2() -> None:
    with pytest.raises(KeyError):
        my_dictionary = {'kris': 'jordan', 'michael': 'jordan'}
        invert(my_dictionary)


def test_favorite_color() -> None: 
    assert favorite_colors({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}) == 'blue'


def test_favorite_color1() -> None:
    assert favorite_colors({'Emma': 'blue', 'Jua': 'yellow', 'Sarah': 'pink', 'Zach': 'orange', 'Cam': 'pink'}) == 'pink'


def test_favorite_color2() -> None:
    assert favorite_colors({'Rice': 'red', 'Stewart': 'red', 'Stone': 'red', 'Kelly': 'red'}) == 'red'


def test_count() -> None:
    assert count(['0', '1', '2']) == ({'0': 1, '1': 1, '2': 1})


def test_count1() -> None:
    assert count(['100', '200', '200']) == ({'100': 1, '200': 2})


def test_count2() -> None:
    assert count(['Emma', 'Cam', 'Zach', 'Anna', 'Eli']) == ({'Emma': 1, 'Cam': 1, 'Zach': 1, 'Anna': 1, 'Eli': 1})