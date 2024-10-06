''' 
Problems:
Number Guessing Game - When we run our program, it generates a random number between 1 and 100
that we have to guess. Now if we type an invalid number like a,  we get an error message, and
the program is giving us feedback, it says this is too high and too low. So the number that the 
computer has generated is between 5 and 10, try until we guess the number and display the message
Congrations! You guessed the number.
'''

# Let's map the Logics here

# Generate a random number
# loop
    # Ask the user to make a guess
    # If not a valid number
    #   print an error
    # If number < guess
    #   print too low
    # if number > guess
    #   print too high
    # else
    #   print well done

# Solution: 

import random

number_to_guess = random.randint(1, 100)
user_input = input('Guess the number between 1 and 100: ')
