"""File to define Fish class."""


class Fish:
    """Fish in the river."""

    age: int

    def __init__(self):
        """New fish in the River ecosystem!"""
        self.age = 0

    def one_day(self):
        """Adds one day to the age of a fish."""
        self.age += 1
