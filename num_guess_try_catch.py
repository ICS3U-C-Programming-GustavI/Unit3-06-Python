#!/usr/bin/env python3
# Created by: Gustav I
# Created on: March 24, 2025
# This program checks if the integer is positive, negative or zero using try catch.

import random  # Import the random module


def main():
    try:
        # Get user's guess
        number_guess = int(input("Guess a number (0-9): "))
        if number_guess < 0 or number_guess > 9:
            print("Please enter a number between 0 and 9.")
        else:
            # Computer chooses a random number
            chosen_number = random.randint(0, 9)

            # Check if the number is right or wrong
            if number_guess == chosen_number:
                print("You got the right number!")
            else:
                print(
                    f"You did not get the right number. The correct number was: {chosen_number}"
                )
    except ValueError:
        print("Invalid input. Please enter an integer between 0 and 9.")


if __name__ == "__main__":
    main()
