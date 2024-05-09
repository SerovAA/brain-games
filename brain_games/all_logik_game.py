import random
import prompt


def generate_question():
    return random.randint(0, 100)


def check_answer(user_name, user_answer, right_answer, counter):
    if user_answer == right_answer:
        print('Correct!')
        return counter + 1
    else:
        print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{right_answer}'")
        print(f"Let's try again, {user_name}!")
        return 4


def brain_game(game_question):
    print(f"Welcome to the Brain Games!\n{game_question}")
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!\n")

    correct_answers_count = 0
    while correct_answers_count < 3:
        question = generate_question()
        right_answer = str(question)
        user_answer = input(f"Question: {question}\nYour answer ")
        correct_answers_count = check_answer(user_name, user_answer, right_answer, correct_answers_count)

    print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    brain_game()
