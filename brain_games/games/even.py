from brain_games.all_logik_game import random_at_100, Brain_Game


def generate_question_answer():
    number = random_at_100()
    question = str(number)
    right_answer = 'yes' if number % 2 == 0 else 'no'
    return question, right_answer


def brain_even():
    Brain_Game(generate_question_answer, 'Answer "yes" if number even otherwise answer "no".')


if __name__ == '__main__':
    brain_even()
