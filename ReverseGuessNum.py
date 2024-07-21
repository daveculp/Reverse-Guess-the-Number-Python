#!/usr/bin/env python3
import random
from math import ceil


print ( """
This is a game of reverse guess the number.
You enter the lower and upper bounds of the 
number to guess.  I will attempt to guess your
number in as few guesses as possible!
""")

num_guesses = 0

lower_bound = int ( input ("Enter the lower limit of the guess: "))
upper_bound = int ( input ("Enter the upper limit of the guess: "))

lower_bound = lower_bound - 1

game_over = False


while game_over == False:
    guess = ceil( ( (upper_bound-lower_bound) / 2) + lower_bound)
    print ("\nIs your number",  guess,"?")
    while True:
        response = input("(Y)es\nToo (H)igh\nToo (Low)\n:")
        response = response.upper()
        if response == "Y":
            game_over = True
            break
        elif response == "H":
            upper_bound = guess
            break
        elif response == "L":
            lower_bound = guess
            break
        else:
            print ('\nI did not understand your response.  Please use only "Y", "H", and "L".')
    num_guesses += 1

print ("\n\nI got it in",num_guesses,"guesses!!")
