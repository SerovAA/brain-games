import random
import prompt


def generate_expression():
    operand1 = random.randint(0, 100)
    operand2 = random.randint(0, 100)
    operator = random.choice(['+', '-', '*'])

    expression = f"{operand1} {operator} {operand2}"
    return expression


def calculate_expression(expression):
    return eval(expression)


def calculator_game():
    print("Welcome to the Calculator Game!")  # Приветствие игрока
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}! \nWhat is the result of the expression?')

    correct_answers_count = 0
    while correct_answers_count < 3:
        expression = generate_expression()
        correct_answer = calculate_expression(expression)
        print(f"Question: {expression}")
        user_answer = input("Your answer: ")
        if int(user_answer) == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break
    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    calculator_game()
