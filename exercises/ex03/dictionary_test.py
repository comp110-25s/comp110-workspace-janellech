"""This program is a the test for dictionary."""

__author__: str = "730714439"

from exercises.ex03.dictionary import invert, favorite_color, count, bin_len
import pytest

"""invert tests"""


def test_invert_use1() -> None:
    assert invert({"hello": "a greeting"}) == {"a greeting": "hello"}


def test_invert_use2() -> None:
    assert invert({"water": "H2O", "desert": "sand"}) == {
        "H2O": "water",
        "sand": "desert",
    }


def test_invert_empty() -> None:
    assert invert({}) == {}


def test_invert_error() -> None:
    with pytest.raises(KeyError):
        my_dictionary = {"aloha": "hi", "molo": "hi"}
        invert(my_dictionary)


def test_count_use1() -> None:
    """first use case test"""
    assert count(["run", "run", "hello"]) == {
        "run": 2,
        "hello": 1,
    }


def test_count_use2() -> None:
    """second use case test"""
    assert count(["pink", "black", "white"]) == {"pink": 1, "black": 1, "white": 1}


def test_count_empty() -> None:
    """edge case"""
    assert count([]) == {}


def test_favorite_color_use1() -> None:
    """first use case test"""
    assert favorite_color({"Bill": "blue", "Bob": "blue"}) == "blue"


def test_favorite_color_use2() -> None:
    """second use case test"""
    assert (
        favorite_color(
            {"Sandy": "green", "John": "purple", "Sally": "purple", "Paul": "green"}
        )
        == "green"
    )


def test_favorite_color_all_tie() -> None:
    """edge case: all values appear once"""
    assert favorite_color({"Sal": "white", "Moses": "blue"}) == "white"


def test_bin_len_use1() -> None:
    """first use case test"""
    assert bin_len(["cats", "five", "I"]) == {4: {"cats", "five"}, 1: {"I"}}


def test_bin_len_use2() -> None:
    """second use case test"""
    assert bin_len(["hi", "hi", "dogs"]) == {2: {"hi", "hi"}, 4: {"dogs"}}


def test_bin_len_empty() -> None:
    """edge case: some empty strings"""
    assert bin_len(["", "fish", "cats"]) == {0: {""}, 4: {"fish", "cats"}}
