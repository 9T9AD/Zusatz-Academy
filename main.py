"""
Prints out a randomly generated addition problem
and checks if the user answers correctly.
"""

import random 

MIN_RANDOM = 10
MAX_RANDOM = 99

num1 = random.randint(MIN_RANDOM, MAX_RANDOM)
num2 = random.randint(MIN_RANDOM, MAX_RANDOM)

#the total_answer variable is the result of num1 + num2
total_answer = num1 + num2

question = int(input(f'What is {num1} + {num2}? '))
user_answer = question
#user_answer is equal to question because of the user input()

if user_answer == total_answer:
    print('Your answer:', user_answer, '\nCorrect!')
else:
    print(f'Your answer: {user_answer} \nIncorrect. The expected answer is {total_answer}')