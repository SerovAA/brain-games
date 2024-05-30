import random


QUESTION = 'What number is missing in the progression?'


def generate_question_answer():
    min_number_random = 1
    max_number_random = 100
    progression_len_min = 5
    progression_len_max = 10
    min_step = 1,
    max_step = 10,
    progression_len = random.randint(progression_len_min, progression_len_max)
    hidden_element_index = random.randint(0, progression_len - 1)
    start_number = random.randint(min_number_random, max_number_random)
    step = random.randint(min_step, max_step)
    progression = [str(start_number + step * i) for i in range(progression_len)]
    progression_with_hidden = list(progression)
    progression_with_hidden[hidden_element_index] = '..'
    question = ' '.join(progression_with_hidden)
    right_answer = str(start_number + step * hidden_element_index)
    return question, right_answer
