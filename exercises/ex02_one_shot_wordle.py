"""EX02 One Shot Wordle."""

__author__ = "730544721"

secret_word: str = "python"
guess: str = input("What is your 6-letter guess?")

count: int = 0
result: str = ""
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

while len(guess) != int(6):
    guess = input("That was not 6 letters! Try again:")

while count < len(secret_word):
    if secret_word[count] == guess[count]:
        result = result + GREEN_BOX
    else:
        tracker: bool = False
        alternate: int = 0
        while not tracker and alternate < len(guess):
            if secret_word[alternate] == guess[count]:
                tracker = True
            else:
                alternate += 1
        if tracker:
            result = result + YELLOW_BOX
        else:
            result = result + WHITE_BOX
    count += 1
print(result)

if str(guess) != "python":
    print("Not quite. Play again soon!")
else:
    print("Woo! You got it!")