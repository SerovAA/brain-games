def getRandom():
    import random
    return random.randint(1, 100)


def checkAnswer(user_Name, user_Answer, right_Answer, counter):
    i = counter
    if user_Answer == right_Answer:
        print('Correct!')
        i += 1
    else:
        print(f"'{user_Answer}' is wrong answer ;(. Correct answer was '{right_Answer}'")
        print(f"Let's try again, {user_Name}!")
        i = 4
    return i


def Brain_Game(Game_Iter, game_Question):
    import prompt
    print(f"Welcome to the Brain Games!\n{game_Question}")
    userName = prompt.string('May I have your name? ')  #
    print(f"Hello, {userName}!\n")

    i = 0
    while i < 3:
        question, right_Answer = Game_Iter()
        userAnswer = input(f"Question: {question}\nYour answer ")
        i = checkAnswer(userName, userAnswer, right_Answer, i)
    if i < 4:
        print(f"Congratulations, {userName}!")


if __name__ == '__main__':
    Brain_Game()