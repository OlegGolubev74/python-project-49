import random
import operator


QUESTION_TEXT = 'What is the result of the expression?'


def get_question_and_corr_answer():
    math_operation = random.choice('+-*')
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    question = f'{str(num1)} {math_operation} {str(num2)}'
    corr_answer = calculate(num1, num2, math_operation)
    return (question, corr_answer)


def calculate(num1, num2, math_operation):
    if math_operation == '+':
        corr_answer = str(operator.add(num1, num2))
    elif math_operation == '-':
        corr_answer = str(operator.sub(num1, num2))
    elif math_operation == '*':
        corr_answer = str(operator.mul(num1, num2))
    return corr_answer
