import random
import prompt


def generate_question_answer():
    number = random.randint(0, 100)
    question = str(number)
    answer = 'yes' if number % 2 == 0 else 'no'
    return question, answer


def brain_even():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}! \nAnswer "yes" if the number is even, otherwise answer "no".')

    correct_answers_count = 0
    while correct_answers_count < 3:
        question, correct_answer = generate_question_answer()
        print("Question:", question)
        user_answer = input("Your answer: ").lower()
        if user_answer == correct_answer:
            print("Correct!")
            correct_answers_count += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break

    print(f"Congratulations, {name}!")


if __name__ == '__main__':
    brain_even()
