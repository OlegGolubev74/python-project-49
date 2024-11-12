import random


QUESTION_TEXT = 'What number is missing in the progression?'


def get_question_and_corr_answer():
    position_hidden_element = random.randint(1, 10)
    progression = get_progression()
    corr_answer = str(progression[position_hidden_element - 1])
    progression[position_hidden_element - 1] = '..'
    question = ' '.join(progression)
    return (question, corr_answer)


def get_games(COUNT_OF_ROUNDS):
    questions = []
    for i in range(COUNT_OF_ROUNDS):
        questions.append(get_question_and_corr_answer())
    return questions


def get_progression():
    start_num = random.randint(1, 10)
    diff = random.randint(1, 10)
    elements_count = 10
    progression = []
    added_num = start_num
    progression.append(str(added_num))
    for item in range(elements_count - 1):
        added_num += diff
        progression.append(str(added_num))
    return progression
