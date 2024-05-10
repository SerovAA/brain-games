import random
from brain_games.all_logik_game import Brain_Game, getRandom


def generate_progression():
    progression_len = random.randint(5, 10)
    hidden_element_index = random.randint(0, progression_len - 1)
    start_number = getRandom()
    step = random.randint(1, 10)

    progression = [str(start_number + step * i) for i in range(progression_len)]
    progression_with_hidden = list(progression)
    progression_with_hidden[hidden_element_index] = '..'

    question = ' '.join(progression_with_hidden)
    correct_answer = str(start_number + step * hidden_element_index)

    return question, correct_answer


def brain_progression():
    Brain_Game(generate_progression, 'What number is missing in the progression?')


if __name__ == '__main__':
    brain_progression()
