import prompt


ROUNDS = 3


def run_brain_game(game_name):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f"Hello, {user_name}!")
    print(game_name.QUESTION)
    round_num = 1
    while round_num <= ROUNDS:
        question, right_answer = game_name.generate_question_answer()
        print(f'Question: {question}')
        user_answer = prompt.string("Your answer: ")
        if user_answer == right_answer:
            print('Correct!')
            round_num += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer was '{right_answer}'.\n"
                  f"Let's try again, {user_name}!")
            break
    else:
        print(f"Congratulations, {user_name}!")
