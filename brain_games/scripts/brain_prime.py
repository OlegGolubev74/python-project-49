#!/usr/bin/env python3
from brain_games.game_engine import play_engine
import brain_games.games.prime


def main():
    count_of_rounds = 3
    play_engine(brain_games.games.prime.get_games(count_of_rounds))


if __name__ == '__main__':
    main()
