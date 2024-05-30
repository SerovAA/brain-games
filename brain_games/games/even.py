import random


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0

def generate_question_answer():
    min_number = 1
    max_number = 100
    number = random.randint(min_number, max_number)
    question = str(number)
    right_answer = 'yes' if is_even(number) else 'no'
    return question, right_answer
