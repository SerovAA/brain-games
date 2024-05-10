import random
from brain_games.all_logik_game import random_at_100, Brain_Game


def generate_expression():
    operand1 = random_at_100()
    operand2 = random_at_100()
    operator = random.choice(['+', '-', '*'])

    expression = f"{operand1} {operator} {operand2}"
    result = str(eval(expression))
    return expression, result


def calculator_game():
    Brain_Game(generate_expression, 'What is the result of the expression?')


if __name__ == '__main__':
    calculator_game()
