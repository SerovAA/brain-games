import random

QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'
def generate_question_answer():
    question = random.randint(1, 100)
    if question == 1:
        return question, "no"
    for i in range(2, (question // 2 + 1)):
        if question % i == 0:
            return question, "no"
    return question, "yes"




