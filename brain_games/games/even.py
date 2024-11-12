import random


QUESTION_TEXT = 'Answer "yes" if the number is '\
                'even, otherwise answer "no".'


def is_even(num):
    return num % 2 == 0


def get_question_and_corr_answer():
    num = random.randint(1, 99)
    question = str(num)
    corr_answer = 'yes' if is_even(num) else 'no'
    return (question, corr_answer)


def get_games(COUNT_OF_ROUNDS):
    questions = []
    for i in range(COUNT_OF_ROUNDS):
        questions.append(get_question_and_corr_answer())
    return questions
