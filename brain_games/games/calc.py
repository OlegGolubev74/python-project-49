import random


# получить вопрос в математическом виде и правильный ответ на него
def get_question_and_corr_answer():
    # вопрос в текстовом виде
    QUESTION_TEXT = 'What is the result of the expression?'

    # определяем аргументы
    math_operation = random.choice('+-*')
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)

    # формируем строку для вопроса в математическом виде
    question = str(num1) + ' ' + math_operation + ' ' + str(num2)

    # вычисляем правильный ответ
    if math_operation == '+':
        corr_answer = str(num1 + num2)
    elif math_operation == '-':
        corr_answer = str(num1 - num2)
    elif math_operation == '*':
        corr_answer = str(num1 * num2)
    # записываем в tuple
    return (question, corr_answer, QUESTION_TEXT)


# получаем наборы (вопрос в математическом виде + правильный ответ)
# количество наборов равно количеству раундов
def get_games(count_of_rounds):
    questions = []
    for i in range(count_of_rounds):
        questions.append(get_question_and_corr_answer())
    return questions
