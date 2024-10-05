''' ***********************************************************************************************************
Problem: Dice Rolling Game
When we execute this program, first, we get question, roll the dice. In this program we have only two options,
yes, or no. If we type anything else, we get an error message saying invalid choice. We can type y, eihter 
lowercase or uppercase, it doesn't matter. And every time we get two new random numbers, just like how we roll
a doce. If we type n, our program terminates and displays a message saying thanks for playing.

***************************************************************************************************************'''

# Loop
    # Ask: roll me dice?
    # If user enters y
    #   Generate two random numbers
    #   Print them
    # If user enters n 
    #   Print thank you message
    #   Terminate
    # Else
    #   Print invalid choice

# solution:

import random

while True:
    choice = input('Roll the dice? (y/n): ').lower()
    if choice == 'y':
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print(f'({die1}, {die2})')
    elif choice == 'n':
        print('Thanks for playing!')
        break
    else: 
        print('Invalid choice!')
