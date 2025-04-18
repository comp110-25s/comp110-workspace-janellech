"""This program calculates the supplies to host a tea party."""

__author__: str = "730714439"


def main_planner(guests: int) -> None:
    """entrypoint"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print(
        "Cost: "
        + "$"
        + str(cost(tea_count=int(guests * 2), treat_count=int(guests * 3)))
    )
    return None


def tea_bags(people: int) -> int:
    """number of tea bags given number of guests"""
    return people * 2


def treats(people: int) -> int:
    """number of treats needed for guests"""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """compute the cost of the tea bags and treats combined"""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
