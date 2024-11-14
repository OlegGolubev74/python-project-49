import random
import math


QUESTION_TEXT = 'Find the greatest common divisor of given numbers.'


def get_question_and_corr_answer():
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    question = str(num1) + ' ' + str(num2)
    corr_answer = str(math.gcd(num1, num2))
    return (question, corr_answer)
