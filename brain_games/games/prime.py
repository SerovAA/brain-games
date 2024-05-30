import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True


def generate_question_answer():
    min_number = 1
    max_number = 100
    number = random.randint(min_number, max_number)
    question = str(number)
    right_answer = 'yes' if is_prime(number) else 'no'
    return question, right_answer
