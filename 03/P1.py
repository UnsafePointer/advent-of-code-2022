from typing import List, Set


def priority(s: str) -> int:
    if s.isupper():
        return ord(s) - 65 + 27
    return ord(s) - 96


def solve() -> int:
    rucksacks: List[List[str]] = [
        list(r.strip()) for r in open("input.txt", "r").readlines()
    ]
    result = 0
    for rucksack in rucksacks:
        left: Set[str] = set(rucksack[0 : int(len(rucksack) / 2)])
        right: Set[str] = set(rucksack[int(len(rucksack) / 2) : len(rucksack)])
        result += priority(left.intersection(right).pop())
    return result


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
