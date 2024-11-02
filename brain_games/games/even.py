import random


# функция проверки числа на четность
def is_even(num):
    if num % 2 == 0:
        corr_answer = 'yes'
    else:
        corr_answer = 'no'
    return corr_answer


# получить вопрос в математическом виде и правильный ответ на него
def get_question_and_corr_answer():
    #  общий вопрос в текстовом виде
    question_text = 'Answer "yes" if the number is '\
                    'even, otherwise answer "no".'
    # определяем аргумент
    num = random.randint(1, 99)
    # формируем строку для вопроса в математическом виде
    question = str(num)
    # определяем правильный ответ на вопрос
    corr_answer = is_even(num)

    return (question, corr_answer, question_text)


# получаем наборы (вопрос в математическом виде + правильный ответ)
# количество наборов равно количеству раундов
def get_games(count):
    result = []
    for i in range(count):
        result.append(get_question_and_corr_answer())
    return result
