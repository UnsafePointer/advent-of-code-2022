from typing import List


def solve() -> int:
    file = open("input.txt", "r")
    datastream: List[str] = list(file.readline().strip())
    buffer_length = 14
    for idx in range(len(datastream) - buffer_length - 1):
        buffer = datastream[idx : idx + buffer_length]
        if len(set(buffer)) == buffer_length:
            return idx + buffer_length
    return -1


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
