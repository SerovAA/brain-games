import random
from math import gcd


QUESTION = 'Find the greatest common divisor of given numbers.'


def generate_question_answer():
    min_number = 1
    max_number = 100
    num1 = random.randint( min_number, max_number)
    num2 = random.randint( min_number, max_number)
    expression = f"{num1} {num2}"
    right_answer = gcd(num1, num2)
    return expression, str(right_answer)
