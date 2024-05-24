import random
from math import gcd


QUESTION = 'Find the greatest common divisor of given numbers.'

def generate_question_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    expression = f"{num1} {num2}"
    right_answer = gcd(num1, num2)
    return expression, str(right_answer)
