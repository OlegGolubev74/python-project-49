import prompt


def play_engine(questions):
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + '!')
    # печатаем вопрос в текстовом виде
    question_text = questions[2]
    print(question_text[2])

    for (question, corr_answer, questions) in questions:
        print('Question: ' + question)
        user_answer = prompt.string('Your answer: ')
        if user_answer == corr_answer:
            print('Correct!')
        else:
            print('"' + user_answer + '"'
                  + ' is wrong answer ;(. Correct answer was '
                  + '"' + corr_answer + '".')
            print("Let\'s try again, " + name + "!")
            return
    print("Congratulations, " + name + '!')
