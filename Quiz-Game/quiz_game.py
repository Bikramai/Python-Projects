# Mapping out the logic

# Define questions, options, correct answer
# Shuffle the questions
# Loop over question
#   Print question
#   Get user input
#   If input is correct
#       Print Correct answer
#       Increase score
#   Else
#       Print wrong answer
# Print the final score

import random
from termcolor import cprint

quiz = [
    {
        'question': 'What is the capital of France?',
        'options': ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'],
        'answer': 'C'
    },
    {
        'question': 'Which planet is known as red planet?',
        'options': ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
        'answer': 'C'
    },
    {
        'question': 'What is the largest ocean on Earth?',
        'options': ['A. Atlantic', 'B. Indian', 'C. Arctic', 'D. Pacific'],
        'answer': 'D'
    }
]

random.shuffle(quiz)


score = 0

for index, item in enumerate(quiz, 1):
    print(f'Question {index}: {item['question']}')
    for option in item['options']:
        print(option)

    answer = input('Your answer: ').upper().strip()

    if answer == item['answer']:
        cprint('Correct!', 'green')
        score += 1
    else:
        cprint(f'Wrong! the correct answer is {item['answer']}', 'red')
        
    print()

print(f'Quiz over! Your final score is {score} out of {len(quiz)}')