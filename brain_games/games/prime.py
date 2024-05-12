from brain_games.all_logik_game import Brain_Game, random_at_100

def question_and_correct_answer():
    question = random_at_100()
    if question == 1:
        return question, "no"
    for i in range(2, (question // 2 + 1)):
        if question % i == 0:
            return question, "no"
    return question, "yes"

def brain_prime():
    Brain_Game(question_and_correct_answer, 'Answer "yes" if given number is prime. Otherwise answer "no".')


if __name__ == '__main__':
    brain_prime()
