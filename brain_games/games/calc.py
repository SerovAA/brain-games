import random
from brain_games.all_logik_game import getRandom, Brain_Game


def generate_expression():
    operand1 = getRandom()
    operand2 = getRandom()
    operator = random.choice(['+', '-', '*'])

    expression = f"{operand1} {operator} {operand2}"
    result = str(eval(expression))
    return expression, result


def calculator_game():
    Brain_Game(generate_expression, 'What is the result of the expression?')


if __name__ == '__main__':
    calculator_game()
