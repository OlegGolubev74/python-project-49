import prompt


COUNT_OF_ROUNDS = 3


def play_engine(question_and_corr_answer, QUESTION_TEXT):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(QUESTION_TEXT)
    round = 0
    while round < COUNT_OF_ROUNDS:
        question, corr_answer = question_and_corr_answer()
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == corr_answer:
            print('Correct!')
            round += 1
        else:
            print(f'"{user_answer}" is wrong answer ;(. '
                  f'Correct answer was "{corr_answer}".')
            print(f'Let\'s try again, {user_name}!')
            return
    print(f'Congratulations, {user_name}!')
