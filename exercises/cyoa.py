"""EX06- Choosing your own adventure."""


__author__ = "730544721"


points: int = 0
player: str = ""


def main() -> None:
    """Entry point of the game."""
    global points
    greet()
    procedure()
    points += function(points)
    repeat: str = input("Would you like to repeat the game? Please answer with yes or no.")
    while repeat == "yes":
        procedure()
        points += function(points)
        repeat = input("Would you like to repeat the game? Please answer with yes or no.")
    exit()


def greet() -> None:
    """Will greet the player before the game starts."""
    global player
    player = input("Hello! What is your name?: ")
    print(f"You have {points} points!")


def procedure() -> None:
    """Will be the main part of the game."""
    global points
    print("What will you choose today?? #1 is a mathematical journey (100 points), #2 is a wordle journey (20 points), and #3 ends the game!")
    choice: int = int(input(f"Hello {player} what choice will you choose today?"))
    if choice > 3:
        print("Oh no! You picked a path that is not listed. Your choice has to be between 1 and 3.")
    while choice <= 3:
        if choice == 1:
            print("Congrats! You decided you want to do some math today... Please answer this question to continue your jouney!!")
            answer = int(input("((200 / 4) / (2.5 + 2.5)) What is the answer?: "))
            if answer != 10:
                points -= 1
            if answer == 10:
                points += 100
            print(f"You have {points} points!") 
        if choice == 2:
            print("Congrats you decided you wanted to do some wordle today! Please guess a 5 letter word to continue your journey! (Hint: it is a common UNC saying!!)")
            secret_word: str = "heels"
            count: int = 0
            result: str = ""
            WHITE_BOX: str = "\U00002B1C"
            GREEN_BOX: str = "\U0001F7E9"
            YELLOW_BOX: str = "\U0001F7E8"
            guess = input("What is your 5 letter word?: ")
            while len(guess) != 5:
                guess = input("That was not 5 letters! Try again:")
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
            if guess == secret_word:
                points += 20
            else:
                points -= 10
                print(f"You have {points} points!") 
        if choice == 3:
            print(f"Your journey is complete! You earned {points} points!")


def function(points: int) -> int:
    """Another possible direction for the player."""
    decision = input(f"Hello, {player} would you like to have a chance to earn extra points? Please print yes or no.")
    if decision == "yes":
        print("Congrats, you just earned 20 extra points!")
        points += 20
    else:
        exit()
    return points


if __name__ == "__main__":
    main()