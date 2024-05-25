import random


QUESTION = 'What number is missing in the progression?'


def generate_question_answer():
    progression_len = random.randint(5, 10)
    hidden_element_index = random.randint(0, progression_len - 1)
    start_number = random.randint(1, 100)
    step = random.randint(1, 10)
    progression = [str(start_number + step * i) for i in range(progression_len)]
    progression_with_hidden = list(progression)
    progression_with_hidden[hidden_element_index] = '..'
    question = ' '.join(progression_with_hidden)
    right_answer = str(start_number + step * hidden_element_index)
    return question, right_answer
