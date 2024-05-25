import random


QUESTION = 'What is the result of the expression?'


def generate_question_answer():
    operand1 = random.randint(1, 100)
    operand2 = random.randint(1, 100)
    operator = random.choice(['+', '-', '*'])

    expression = f"{operand1} {operator} {operand2}"
    right_answer = str(eval(expression))
    return expression, right_answer