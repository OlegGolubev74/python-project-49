#!/usr/bin/env python3

import prompt
import random


def main():
    number_rounds = 3
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print("Hello, " + name + '!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    round = 0
    while round < number_rounds:
        question = random.randint(1, 99)
        # сразу определяем правильный ответ на вопрос
        if question % 2 == 0:
            corr_answer = 'yes'
        else:
            corr_answer = 'no'
        print(('Question: ' + str(question)))
        answer = prompt.string('Your answer: ')
        if answer == corr_answer:
            print('Correct!')
            round += 1
        else:
            print('"' + answer + '"'
                  + ' is wrong answer ;(. Correct answer was '
                  + '"' + corr_answer + '".')
            print("Let\'s try again, " + name + "!")
            break

    if round == number_rounds:
        print("Congratulations, " + name + '!')


if __name__ == '__main__':
    main()
