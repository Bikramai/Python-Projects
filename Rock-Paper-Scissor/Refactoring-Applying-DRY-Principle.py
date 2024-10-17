'''**********************************************************************************************
Problem:
Rock, Paper, Scissor Game. How it works, First we get a question, rock, paper, or scissors.
Here we only have three choices, R, P, or S. If we type anuthin else, we get an error message 
saying invalid choice. Now let me go with R, that is short for rock, so I chose rock, 
computer chose paper, and I lost. Now right after we get asked if we want to continue, 
let's try again, this time I'm going to go with scissors, so I chose scissors, 
computer chose paper, I won.If you want to stop type n, the game ends.
************************************************************************************************'''

# Solution:
# Mapping the Logics

# Ask the user to make a choice
# If choice is not valid
#   Print an error
# Let the computer to make a choice
# Print choices (emojis)
# Determine the winner
# Ask the user if they want to continue
# If not
#   Terminate


import random

ROCK = 'r'
SCISSORS = 's'
PAPER = 'p'
emojis = {ROCK: '🪨', SCISSORS: '✂️', PAPER: '📃' }
choices = (tuple(emojis.keys()))


def get_user_choice():
    while True:
        user_choice = input('Rock, Paper, or Scissors? (r/p/s): ').lower()
        if user_choice in choices:
            return user_choice
        else:
            print('Invalid choice!')

def display_choices(user_choice, computer_choice):
    print(f'You chose {emojis[user_choice]}')
    print(f'Computer chose {emojis[computer_choice]}')
            
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print('Tie!')
    elif (
    (user_choice == ROCK and computer_choice == SCISSORS) or 
    (user_choice == SCISSORS and computer_choice == PAPER) or 
    (user_choice == PAPER and computer_choice == ROCK)):
        print('You win')
    else:
        print('You lose')          
    
def play_game():
    while True:
        user_choice = get_user_choice()

        computer_choice = random.choice(choices)

        display_choices(user_choice, computer_choice)

        determine_winner(user_choice, computer_choice)

        should_continue = input('Continue? (y/n): ').lower()
        if should_continue == 'n':
            break

play_game()