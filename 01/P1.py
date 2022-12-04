from typing import List


def solve() -> int:
    file = open("input.txt", "r")

    current_calories = 0
    elves: List[int] = []
    for line in file:
        line = line.strip()
        if not line:
            elves.append(current_calories)
            current_calories = 0
        else:
            current_calories += int(line)
    elves.append(current_calories)
    return max(elves)


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
