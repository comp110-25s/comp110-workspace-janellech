"""This program is a the test for dictionary."""

__author__: str = "730714439"

from exercises.ex03.dictionary import invert
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import bin_len
import pytest


def test_invert() -> None:
    """testing invert function"""
    """first use case test"""
    assert invert({"hello": "a greeting"}) == {"a greeting": "hello"}
    """second use case test"""
    assert invert({"water": "H2O", "desert": "sand"}) == {
        "H2O": "water",
        "sand": "desert",
    }
    """edge case: empty dict"""
    assert invert({}) == {}
    """test KeyError"""
    with pytest.raises(KeyError):
        my_dictionary = {"aloha": "hi", "molo": "hi"}
        invert(my_dictionary)


def test_count() -> None:
    """first use case test"""
    assert count(["run", "run", "hello"]) == {
        "run": 2,
        "hello": 1,
    }
    """ second use case test"""
    assert count(["pink", "black", "white"]) == {"pink": 1, "black": 1, "white": 1}
    """edge case"""
    assert count([]) == {}


def test_favorite_color() -> None:
    """first use case test"""
    assert favorite_color({"Bill": "blue", "Bob": "blue"}) == "blue"
    """second use case test"""
    assert (
        favorite_color(
            {"Sandy": "green", "John": "purple", "Sally": "purple", "Paul": "green"}
        )
        == "green"
    )
    """edge case: all values appear once"""
    assert favorite_color({"Sal": "white", "Moses": "blue"}) == "white"


def test_bin_len() -> None:
    """first use case test"""
    assert bin_len(["cats", "five", "I"]) == {4: {"cats", "five"}, 1: {"I"}}
    """ second use case test"""
    assert bin_len(["hi", "hi", "dogs"]) == {2: {"hi", "hi"}, 4: {"dogs"}}
    """edge case: some empty strings"""
    assert bin_len(["", "fish", "cats"]) == {0: {""}, 4: {"fish", "cats"}}
