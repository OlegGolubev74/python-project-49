import random


# функция проверки числа на простоту
def prime_or_not(num):
    if num > 1:
        d = 2
        while num % d != 0:
            d += 1
        return d == num


# получить вопрос в математическом виде и правильный ответ на него
def get_question_and_corr_answer():
    #  общий вопрос в текстовом виде
    QUESTION_TEXT = 'Answer "yes" if given number is prime. '\
                    'Otherwise answer "no".'
    # определяем аргумент
    num = random.randint(1, 50)
    # формируем строку для вопроса в математическом виде
    question = str(num)
    # определяем правильный ответ
    if prime_or_not(num) is True:
        corr_answer = 'yes'
    else:
        corr_answer = 'no'

    # записываем в tuple
    return (question, corr_answer, QUESTION_TEXT)


# получаем наборы (вопрос в математическом виде + правильный ответ)
# количество наборов равно количеству раундов
def get_games(count_of_rounds):
    questions = []
    for i in range(count_of_rounds):
        questions.append(get_question_and_corr_answer())
    return questions
