from brain_games.all_logik_game import random_at_100, Brain_Game


def generate_expression():
    num1 = random_at_100()
    num2 = random_at_100()
    expression = f"{num1} {num2}"
    gcd = find_gcd(num1, num2)
    return expression, str(gcd)


def find_gcd(num1, num2):
    while num2:
        num1, num2 = num2, num1 % num2
    return num1


def gcd_game():
    Brain_Game(generate_expression,
               'Find the greatest common divisor of given numbers.')


if __name__ == '__main__':
    gcd_game()
