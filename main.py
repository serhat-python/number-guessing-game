import random
from art import logo

print("Welcome to the Number Guessing game!")
print("I'm thinking of a number between 1 and 100.")


def guess_the_number():
    print(logo)
    attempts = 0
    num = random.randint(1, 100)
    choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

    if choice == "easy":
        attempts = 10
    elif choice == "hard":
        attempts = 5
    else:
        attempts = 1

    print(f"You have {attempts} attempts remaining to guess the number")

    while attempts != 0:
        user_num = int(input("Guess a number between 1 and 100: "))

        if user_num == num:
            print("You guessed the right number. You win")
            return
        elif user_num < num:
            print(f"Too low. Guess again")
        elif user_num > num:
            print(f"Too high. Guess again")

        if user_num != num:
            attempts -= 1
            print(f"You have {attempts} remaining guesses!")
            if attempts == 0:
                print(f"You lose the right number was {num}")


guess_the_number()

