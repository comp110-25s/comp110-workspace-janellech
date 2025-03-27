"""This program is a dictionary."""

__author__: str = "730714439"


def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """inverts keys and values with unique keys"""
    inverted_dict = {}
    for key in dictionary:
        values = dictionary[key]
        if values in inverted_dict:
            raise KeyError("That word is already in the dictionary! Enter a new word!")
        inverted_dict[values] = key
    return inverted_dict


def count(values: list[str]) -> dict[str, int]:
    """Each key is unique and each value is the count of
    appearances of the key in the input."""
    result = {}
    for key in values:
        if key in result:
            result[key] += 1
        else:
            result[key] = 1
    return result


def favorite_color(names_colors: dict[str, str]) -> str:
    """Returns color that appears most frequently as favorite."""
    colors = []
    fav_color = ""
    max_count = 0

    """get just colors not names from dictionary and add to list"""
    for name in names_colors:
        color = names_colors[name]
        colors.append(color)
    """count how many times the colors appear"""
    color_count = {}
    for color in colors:
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
    """color that appears most"""
    for color in color_count:
        temp_count = color_count[color]
        if temp_count > max_count:
            fav_color = color
            max_count = temp_count
    return fav_color


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Bins list of strings where keys are string lengths,
    and values are sets of words of that length."""
    result = {}
    for word in words:
        length = len(word)
        if length not in result:
            result[length] = set()
        result[length].add(word)
    return result
