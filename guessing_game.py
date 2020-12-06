# Program to guess a number between 1 to 9 till the guess is correct
# Importing the random library
import random

# Generating a random value
number = random.randint(1, 9)

# Checking the condition
while True:
    guess = int(input("Enter a number between 1 and 9, 9 can also be included, until you get it right: "))
    if number == guess:
        print("Well guessed!")
        break
