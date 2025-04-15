"""File to define River class."""

__author__: str = "730714439"

from exercises.EX04.fish import Fish
from exercises.EX04.bear import Bear


class River:
    """This is the river ecosystem object."""

    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears!"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Check ages of surviving animals and update population!"""
        survive_fish: list[Fish] = []
        survive_bears: list[Bear] = []

        for fish in self.fish:
            if fish.age <= 3:
                survive_fish.append(fish)
        self.fish = survive_fish

        for bear in self.bears:
            if bear.age <= 5:
                survive_bears.append(bear)
        self.bears = survive_bears

    def bears_eating(self):
        """Bears eating fish if there are enough fish and removing eaten fish."""
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)

    def check_hunger(self):
        """Check how hungry a bear is and remove hungry bears."""
        alive_bears: list[Bear] = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                alive_bears.append(bear)
        self.bears = alive_bears

    def repopulate_fish(self):
        """Add fish to the river ecosystem."""
        num_new_fish = (len(self.fish) // 2) * 4
        for _ in range(num_new_fish):
            self.fish.append(Fish())

    def repopulate_bears(self):
        """Add bears to the river ecosystem!"""
        num_new_bears = len(self.bears) // 2
        for _ in range(num_new_bears):
            self.bears.append(Bear())

    def view_river(self):
        """Status of the bear and fish populations."""
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")

    def one_river_day(self):
        """Simulate one day of life in the river!"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulate one week in the river ecosystem!"""
        days_in_week = 0
        while days_in_week < 7:
            self.one_river_day()
            days_in_week += 1

    def remove_fish(self, amount: int):
        """Remove fish from river."""
        idx: int = 0
        while idx < amount:
            self.fish.pop(idx)
            idx += 1
        return self.fish
