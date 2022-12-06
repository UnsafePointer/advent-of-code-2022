from typing import List


def solve() -> int:
    file = open("input.txt", "r")
    datastream: List[str] = list(file.readline().strip())
    for idx in range(len(datastream) - 3):
        buffer = datastream[idx : idx + 4]
        if len(set(buffer)) == 4:
            return idx + 4
    return -1


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
