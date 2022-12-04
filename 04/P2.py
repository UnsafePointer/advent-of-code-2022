from typing import List, Tuple


def solve() -> int:
    pairs: List[Tuple[Tuple[int, int], Tuple[int, int]]] = []

    file = open("input.txt", "r")
    for line in file:
        pairs.append(
            tuple(
                [tuple([int(s) for s in t.split("-")]) for t in line.strip().split(",")]
            )
        )
    result = 0
    for ((l_start, l_end), (r_start, r_end)) in pairs:
        if l_end < r_start or r_end < l_start:
            result += 1
    return len(pairs) - result


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
