def random_at_100():
    import random
    return random.randint(1, 100)


def check_answer(user_Name, user_Answer, right_Answer, counter):
    i = counter
    if user_Answer == right_Answer:
        print('Correct!')
        i += 1
    else:
        print(f"'{user_Answer}' "
              f"is wrong answer ;(. Correct answer was '{right_Answer}'")
        print(f"Let's try again, {user_Name}!")
        i = 4
    return i


def Brain_Game(Game_Iter, game_Question):
    import prompt
    print(f"Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')  #
    print(f"Hello, {user_name}!\n{game_Question}")

    i = 0
    while i < 3:
        question, right_Answer = Game_Iter()
        user_Answer = input(f"Question: {question}\nYour answer ")
        i = check_answer(user_name, user_Answer, right_Answer, i)
    if i < 4:
        print(f"Congratulations, {user_name}!")


if __name__ == '__main__':
    Brain_Game()
