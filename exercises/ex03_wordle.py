"""EX03 Structured Wordle."""

__author__ = "730544721"


def contains_char(search: str, single_character: str) -> bool:
    """Will return True if single character is found at any index and return False if not."""
    assert len(single_character) == 1
    count: int = 0
    while count < len(search):
        if search[count] == single_character:
            return True
        count += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Will return an emoji if the two strings are the same length and where the variable is."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    YELLOW_BOX: str = "\U0001F7E8"
    GREEN_BOX: str = "\U0001F7E9"
    result: str = ""
    count: int = 0
    while count < len(secret):
        if guess[count] == secret[count]:
            result += GREEN_BOX
        else:
            x: bool = contains_char(secret, guess[count])
            if x is True:
                result += YELLOW_BOX
            else:
                result += WHITE_BOX
        count += 1
    return result


def input_guess(e: int) -> str:
    """Will tell user to provide a guess of expected length and do so until did."""
    guess: str = input(f"Enter a {e} character word: ")
    while len(guess) != e:
        guess = input(f"That wasn't {e} chars! Try again: code")
    return guess


def main() -> None:
    """The entrypoint of the program and main game loop."""
    secret_word: str = "codes"
    tries: int = 1
    x: bool = False
    while tries <= 6 and not x:
        print(f"=== Turn {tries}/6 ===")
        guess = input_guess(len(secret_word))
        print(emojified(guess, secret_word))
        if guess == secret_word:
            x = True
        tries += 1
    if x:
        print(f"You won in {tries - 1}/6 turns!")
    else:
        print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main()