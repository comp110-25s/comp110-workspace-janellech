"""This program is a fun Wordle program."""

__author__: str = "730714439"


def contains_char(word: str, single: str) -> bool:
    """Test if single character string is found in first string"""
    assert len(single) == 1, f"len('{single}') is not 1"
    idx: int = 0
    while idx < len(word):
        if word[idx] == single:
            return True
        idx = idx + 1
    return False


"""Named constants for emojification"""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"


def emojified(guess: str, secret: str) -> str:
    """Return string of emojis based on accuracy of guess"""
    assert len(guess) == len(secret), "Guess must be same length as secret"
    idx: int = 0
    result: str = ""
    while idx < len(guess):
        if guess[idx] == secret[idx]:
            result = result + GREEN_BOX
        elif contains_char(secret, guess[idx]):
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
        idx = idx + 1
    return result


def input_guess(expected_length: int) -> str:
    """Prompt user for a guess of the expected length."""
    guess = input(f"Enter a {expected_length} character word: ")
    while len(guess) != expected_length:
        guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    """Define variables:"""
    possible_turns = 6
    turns_spent = 0
    user_win = False

    """Begin game loop:"""
    while possible_turns > turns_spent and not user_win:
        turns_spent += 1
        print(f"=== Turn {turns_spent}/{possible_turns} ===")
        guess_right_n = input_guess(len(secret))
        print(emojified(guess_right_n, secret))

        if guess_right_n == secret:
            user_win = True

    """Printing win or loss:"""
    if user_win:
        print(f"You won in {turns_spent}/6 turns!")
    else:
        print(f"X/{possible_turns} - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
