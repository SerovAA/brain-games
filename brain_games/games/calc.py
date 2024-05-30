import random


QUESTION = 'What is the result of the expression'


def generate_question_answer():
    min_number = 1
    max_number = 100
    operand1 = random.randint(min_number, max_number)
    operand2 = random.randint(min_number, max_number)
    operator = random.choice(['+', '-', '*'])

    expression = f"{operand1} {operator} {operand2}"
    right_answer = str(eval(expression))
    return expression, right_answer
