#!/usr/bin/env python3
from brain_games.game_engine import play_engine
from brain_games.games.gcd import get_games


def main():
    count_of_rounds = 3
    play_engine(get_games(count_of_rounds))


if __name__ == '__main__':
    main()
