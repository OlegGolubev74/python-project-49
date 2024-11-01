import random


# получить вопрос в математическом виде и правильный ответ на него
def get_question_and_corr_answer():
    # вопрос в текстовом виде
    question_text = 'Find the greatest common divisor of given numbers.'
    # определяем аргументы
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    # формируем строку для вопроса в математическом виде
    question = str(num1) + ' ' + str(num2)

    # вычисляем правильный ответ
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1

    corr_answer = str(num1 + num2)

    # записываем в tuple
    return (question, corr_answer, question_text)


# получаем наборы (вопрос в математическом виде + правильный ответ)
# количество наборов равно количеству раундов
def get_games(count):
    result = []
    for i in range(count):
        result.append(get_question_and_corr_answer())
    return result
