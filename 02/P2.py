from __future__ import annotations
from enum import Enum, auto
from typing import Dict


class Result(Enum):
    WIN = 6
    DRAW = 3
    LOSE = 0


class Play(Enum):
    ROCK = 1
    PAPER = 2
    SCISSOR = 3

    def resolve(self, result: Result) -> Play:
        if result == result.DRAW:
            return self

        mapping: Dict[Play, Play] = {
            Play.ROCK: Play.SCISSOR,
            Play.PAPER: Play.ROCK,
            Play.SCISSOR: Play.PAPER,
        }
        if result == Result.LOSE:
            return mapping[self]

        inverse_mapping = {v: k for k, v in mapping.items()}
        return inverse_mapping[self]


def create_play(s: str) -> Play:
    if s == "A":
        return Play.ROCK
    elif s == "B":
        return Play.PAPER
    else:  # s == 'C':
        return Play.SCISSOR


def create_result(s: str) -> Result:
    if s == "X":
        return Result.LOSE
    elif s == "Y":
        return Result.DRAW
    else:  # s == 'Z':
        return Result.WIN


def resolve_play(play: Play, result: Result) -> int:
    other_play = play.resolve(result)

    return result.value + other_play.value


def solve() -> int:
    file = open("input.txt", "r")

    total = 0
    for (p, r) in [tuple(line.strip().split(" ")) for line in file]:
        play = create_play(p)
        result = create_result(r)
        total += resolve_play(play, result)
    return total


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
