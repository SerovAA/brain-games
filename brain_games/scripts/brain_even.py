#!/usr/bin/env python3
from brain_games.engine import run_brain_game
from brain_games.games import even


def main():
    run_brain_game(even)


if __name__ == '__main__':
    main()
