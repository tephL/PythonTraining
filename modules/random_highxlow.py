#high or low num guessing
import random

low = 1
high = 100
guesses = 0

secretnum = random.randint(low, high)

while True:
    guess = int(input(f"Guess the number {low} - {high}: "))
    guesses += 1
    
    if guess > secretnum:
        print(f"{guess} is too high\n")
    elif guess < secretnum:
        print(f"{guess} is too low\n")
    else:
        print(f"{guess} is correct!\nYou took {guesses} attempts.")