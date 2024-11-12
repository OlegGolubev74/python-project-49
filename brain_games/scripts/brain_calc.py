#!/usr/bin/env python3
from brain_games.game_engine import play_engine
import brain_games.games.calc


def main():
    COUNT_OF_ROUNDS = 3
    play_engine(brain_games.games.calc.get_games(COUNT_OF_ROUNDS),
                brain_games.games.calc.QUESTION_TEXT)


if __name__ == '__main__':
    main()
