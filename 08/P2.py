from typing import List, Tuple
from sys import maxsize


def scenic_score(grid: List[List[int]], position: Tuple[int, int]) -> int:
    (x, y) = position
    value = grid[x][y]

    # North
    total_n_visible = 0
    for n_pos in range(y - 1, -1, -1):
        total_n_visible += 1
        if value <= grid[x][n_pos]:
            break

    # South
    total_s_visible = 0
    for n_pos in range(y + 1, len(grid), 1):
        total_s_visible += 1
        if value <= grid[x][n_pos]:
            break

    # West
    total_w_visible = 0
    for n_pos in range(x - 1, -1, -1):
        total_w_visible += 1
        if value <= grid[n_pos][y]:
            break

    # East
    total_v_visible = 0
    for n_pos in range(x + 1, len(grid[y]), 1):
        total_v_visible += 1
        if value <= grid[n_pos][y]:
            break

    return total_n_visible * total_s_visible * total_w_visible * total_v_visible


def solve() -> int:
    file = open("input.txt", "r")
    grid: List[List[int]] = [
        [int(c) for c in line.strip()] for line in file.readlines()
    ]
    result = -maxsize
    for (y, row) in enumerate(grid):
        for (x, _) in enumerate(row):
            if x == 0 or x == len(grid) - 1:
                continue
            elif y == 0 or y == len(grid) - 1:
                continue
            result = max(result, scenic_score(grid=grid, position=(x, y)))

    return result


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
