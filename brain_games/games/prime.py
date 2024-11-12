import random


QUESTION_TEXT = 'Answer "yes" if given number is prime. '\
                'Otherwise answer "no".'


def is_prime(num):
    if num > 1:
        d = 2
        while num % d != 0:
            d += 1
        return d == num


def get_question_and_corr_answer():
    num = random.randint(1, 50)
    question = str(num)
    corr_answer = 'yes' if is_prime(num) else 'no'
    return (question, corr_answer)


def get_games(COUNT_OF_ROUNDS):
    questions = []
    for i in range(COUNT_OF_ROUNDS):
        questions.append(get_question_and_corr_answer())
    return questions
