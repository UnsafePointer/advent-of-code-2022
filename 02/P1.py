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

    def resolve(self, other: Play) -> Result:
        if self == other:
            return Result.DRAW

        mapping: Dict[Play, Play] = {
            Play.ROCK: Play.SCISSOR,
            Play.PAPER: Play.ROCK,
            Play.SCISSOR: Play.PAPER,
        }
        if mapping[self] == other:
            return Result.WIN
        return Result.LOSE


def create_play(s: str) -> Play:
    if s == "A" or s == "X":
        return Play.ROCK
    elif s == "B" or s == "Y":
        return Play.PAPER
    else:  # s == 'C' or s == 'Z':
        return Play.SCISSOR


def resolve_play(p1: Play, p2: Play) -> int:
    return p2.resolve(p1).value + p2.value


def solve() -> int:
    file = open("input.txt", "r")
    result = 0
    for (p1, p2) in [
        tuple([create_play(p) for p in line.strip().split(" ")]) for line in file
    ]:
        result += resolve_play(p1, p2)
    return result


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
