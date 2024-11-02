import random


def get_question_and_corr_answer():
    # вопрос в текстовом виде
    question_text = 'What number is missing in the progression?'
    # Первый член
    num1 = random.randint(1, 10)
    # Разность
    diff = random.randint(1, 10)
    # Количество членов
    elements_count = 10
    # член, который скрывается точками и который и равен верному ответу
    position_hidden_element = random.randint(1, 10)
    # создаем список, куда будем записывать члены прогрессии
    # и сразу добавлили в список первый член
    added_number = num1
    progression = []
    progression.append(added_number)
    # делаем список с прогрессией
    for num1 in range(elements_count - 1):
        added_number += diff
        progression.append(added_number)

    # формируем строку question для вопроса
    # и определяем правильный ответ corr_answer
    question = ''
    for i in range(len(progression)):
        if question == '':  # если первый член, то пробел перед ним не нужен
            if position_hidden_element == i + 1:
                question = '..'
                corr_answer = str(progression[i])
            else:
                question = str(progression[i])
        else:  # не первый член, перед ним ставим пробел
            if position_hidden_element == i + 1:
                question += ' ' + '..'
                corr_answer = str(progression[i])
            else:
                question += ' ' + str(progression[i])

    return (question, corr_answer, question_text)


# получаем наборы (вопрос в математическом виде + правильный ответ)
# количество наборов равно количеству раундов
def get_games(count):
    result = []
    for i in range(count):
        result.append(get_question_and_corr_answer())
    return result
