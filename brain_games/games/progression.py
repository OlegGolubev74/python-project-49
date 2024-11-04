import random


def get_question_and_corr_answer():
    # вопрос в текстовом виде
    QUESTION_TEXT = 'What number is missing in the progression?'
    # Первый член
    start_num = random.randint(1, 10)
    # Разность
    diff = random.randint(1, 10)
    # Количество членов
    elements_count = 10
    # член, который скрывается точками и который и равен верному ответу
    position_hidden_element = random.randint(1, 10)
    # создаем список, куда будем записывать члены прогрессии
    # и сразу добавлили в список первый член
    progression = []
    added_num = start_num
    progression.append(str(added_num))
    for item in range(elements_count - 1):
        added_num += diff
        progression.append(str(added_num))

    # заменяем точками скрытый элемент, который и равен правильному ответу
    corr_answer = str(progression[position_hidden_element - 1])
    progression[position_hidden_element - 1] = '..'
    # делаем из списак строку
    question = ' '.join(progression)

    return (question, corr_answer, QUESTION_TEXT)


# получаем наборы (вопрос в математическом виде + правильный ответ)
# количество наборов равно количеству раундов
def get_games(count_of_rounds):
    questions = []
    for i in range(count_of_rounds):
        questions.append(get_question_and_corr_answer())
    return questions
