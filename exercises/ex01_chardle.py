"""EX01 - Chardle - A cute step toward Wordle."""
__author__ = "730544721"


first_word:str = input("Enter a 5-character word: ")
if len(first_word) != 5:
    print("Error: Word must contain 5 characters")
    exit()
character:str = input("Enter a single character: ")
if len(character) != 1:
    print("Error: Character must be a single character")
    exit()
count: int = 0


print("Searching for " + character + " in " + first_word)

if character == first_word[0]:
    print(character + " is found at index 0 ")
    count += 1 
if character == first_word[1]:
    print(character + " is found at index 1 ")
    count += 1
if character == first_word[2]:
    print(character + " is found at index 2 ")
    count += 1
if character == first_word[3]:
    print(character + " is found at index 3 ")
    count += 1
if character == first_word[4]:
    print(character + " is found at index 4 ")
    count += 1

if count == 1:
    print(str(count) + " instance of " + character + " found in " + first_word)
if count > 1:
    print(f"{count} instances of {character} found in {first_word}")
if count == 0:
    print("No instances of " + count + " found in " + first_word)
