#!/usr/bin/env python3
from brain_games.game_engine import play_engine
import brain_games.games.calc


def main():
    play_engine(brain_games.games.calc.get_question_and_corr_answer,
                brain_games.games.calc.QUESTION_TEXT)


if __name__ == '__main__':
    main()
