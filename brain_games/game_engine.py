import prompt


def play_engine(questions, QUESTION_TEXT):
    print("Welcome to the Brain Games!")
    user_name = prompt.string('May I have your name? ')
    print(f'Hello, {user_name}!')
    print(QUESTION_TEXT)
    for (question, corr_answer) in questions:
        print(f'Question: {question}')
        user_answer = prompt.string('Your answer: ')
        if user_answer == corr_answer:
            print('Correct!')
        else:
            print(f'"{user_answer}" is wrong answer ;(. '
                  f'Correct answer was "{corr_answer}".')
            print(f'Let\'s try again, {user_name}!')
            return
    print(f'Congratulations, {user_name}!')
