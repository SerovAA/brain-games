import random


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_question_answer():
    number = random.randint(1, 100)
    question = str(number)
    right_answer = 'yes' if number % 2 == 0 else 'no'
    return question, right_answer