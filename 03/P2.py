from typing import List, Set
import itertools


def priority(s: str) -> int:
    if s.isupper():
        return ord(s) - 65 + 27
    return ord(s) - 96


def solve() -> int:
    rucksacks: List[List[str]] = [
        list(r.strip()) for r in open("input.txt", "r").readlines()
    ]
    result = 0
    while rucksacks:
        first = set(rucksacks.pop(0))
        second = set(rucksacks.pop(0))
        third = set(rucksacks.pop(0))
        result += priority(first.intersection(second).intersection(third).pop())
    return result


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
