import random
from termcolor import cprint

QUESTION = 'question'
OPTIONS = 'options'
ANSWER = 'answer'

quiz = [
    {
        QUESTION: 'What is the capital of France?',
        OPTIONS: ['A. Berlin', 'B. Madrid', 'C. Paris', 'D. Rome'],
        ANSWER: 'C'
    },
    {
        QUESTION: 'Which planet is known as red planet?',
        OPTIONS: ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
        ANSWER: 'C'
    },
    {
        QUESTION: 'What is the largest ocean on Earth?',
        OPTIONS: ['A. Atlantic', 'B. Indian', 'C. Arctic', 'D. Pacific'],
        ANSWER: 'D'
    }
]

random.shuffle(quiz)


score = 0

for index, item in enumerate(quiz, 1):
    print(f'Question {index}: {item[QUESTION]}')
    for option in item[OPTIONS]:
        print(option)

    answer = input('Your answer: ').upper().strip()

    if answer == item[ANSWER]:
        cprint('Correct!', 'green')
        score += 1
    else:
        cprint(f'Wrong! the correct answer is {item[ANSWER]}', 'red')
        
    print()

print(f'Quiz over! Your final score is {score} out of {len(quiz)}')