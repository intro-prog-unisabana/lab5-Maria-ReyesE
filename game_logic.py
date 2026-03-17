from secret_number import *
from response import *

seed = int(input("Enter a seed number:\n"))
seed_secret_numbers(seed)

secret = generate_secret_number()

tries = 0

while True:
    guess = int(input("What is your guess:\n"))
    tries += 1

    message, correct = input_response(secret, guess)
    print(message)

    if correct:
        print(f"It took you {tries} tries!")
        break