"""File to define Bear class."""


class Bear:
    """Bears living by the river."""

    age: int
    hunger_score: int

    def __init__(self):
        """A new bear in the river ecosystem!"""
        self.age = 0
        self.hunger_score = 0

    def one_day(self):
        """Calculates the age and hunger of a bear!"""
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        """Calculates a bear's hunger score based on the number of fish eaten."""
        self.hunger_score += num_fish
