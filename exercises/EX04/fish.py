"""File to define Fish class."""


class Fish:
    """Fish in the river."""

    age: int

    def __init__(self):
        self.age = 0

    def one_day(self):
        self.age += 1
