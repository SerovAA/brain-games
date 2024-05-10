from brain_games.all_logik_game import Brain_Game, getRandom

def question_and_correct_answer():
    question = getRandom()
    if question == 1:
        return question, "no"
    for i in range(2, (question // 2 + 1)):
        if question % i == 0:
            return question, "no"
    return question, "yes"

def brain_prime():
    Brain_Game(question_and_correct_answer, 'Answer "yes" if given number is prime. Otherwise answer "no"')


if __name__ == '__main__':
    brain_prime()
