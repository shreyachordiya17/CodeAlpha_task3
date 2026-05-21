import random

print("===================================")
print("        HANGMAN WORD GAME          ")
print("===================================")

name = input("Enter Your Name: ")

print("\nHello", name + "!")
print("Try to guess the hidden word")
print("You have only 6 chances")

word_list = [
    "notebook",
    "hospital",
    "umbrella",
    "sandwich",
    "football",
    "building",
    "airplane",
    "mountain",
    "festival",
    "computer",
    "language",
    "backpack",
    "elephant",
    "keyboard",
    "diamond"
]

secret_word = random.choice(word_list)

guessed_letters = ""

turns = 6

print("\nLet's Start The Game!")

while turns > 0:

    failed = 0

    print("\nWord :", end=" ")

    for char in secret_word:

        if char in guessed_letters:
            print(char, end=" ")

        else:
            print("_", end=" ")
            failed += 1

    print()

    if failed == 0:
        print("\nCongratulations", name + "!")
        print("You guessed the correct word")
        print("The word was :", secret_word)
        break

    guess = input("\nGuess a letter: ").lower()

    if len(guess) > 1:
        print("Please enter only one letter")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter")

    guessed_letters += guess

    if guess not in secret_word:

        turns -= 1

        print("Wrong Guess")

        print("Remaining Chances:", turns)

        if turns == 5:
            print("Hint: It is a common object or place")

        elif turns == 4:
            print("Keep trying carefully")

        elif turns == 3:
            print("Half chances are gone")

        elif turns == 2:
            print("Only 2 chances left")

        elif turns == 1:
            print("Last chance remaining")

        elif turns == 0:
            print("\nGame Over!")
            print("Better Luck Next Time")
            print("Correct Word was :", secret_word)