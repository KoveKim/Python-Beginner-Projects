# Guessing game program!
# The user keeps typing different responses until they guess the secret word.

def main(secret_word):  # Main game
    user_guess = ""
    tries = 3

    while user_guess != secret_word:  # Run program until correct answer is given
        user_guess = input("Guess the secret word! (Tries remaining: " + str(tries) + "): ")

        if user_guess == secret_word:
            print("Correct! You win!\n")
        elif tries != 0 and user_guess != secret_word:
            print("Incorrect!\n")
            tries -= 1
            if tries == 0:
                print("Sorry, you lose this round. Try again!\n")
                tries = 3


print("Hint: Domesticated animal\n")
main("cat")  # Calling the function with a param so the answer can be changed

print("That round was easy. Now try this one...")
print("Hint: Common color\n")
main("blue")

print("Ok, you're good. Last round.")
print("Hint: Car manufacturer. No capital letters.\n")
main("mazda")

print("Congratulations! Thanks for playing my game. -Khristian")
