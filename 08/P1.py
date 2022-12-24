from typing import List, Tuple


def is_tree_visible(grid: List[List[int]], position: Tuple[int, int]) -> bool:
    (x, y) = position
    value = grid[x][y]

    # North
    n_visible = True
    for n_pos in range(y - 1, -1, -1):
        if value <= grid[x][n_pos]:
            n_visible = False
            break

    # South
    s_visible = True
    for n_pos in range(y + 1, len(grid), 1):
        if value <= grid[x][n_pos]:
            s_visible = False
            break

    # West
    w_visible = True
    for n_pos in range(x - 1, -1, -1):
        if value <= grid[n_pos][y]:
            w_visible = False
            break

    # East
    e_visible = True
    for n_pos in range(x + 1, len(grid[y]), 1):
        if value <= grid[n_pos][y]:
            e_visible = False
            break

    return n_visible or s_visible or w_visible or e_visible


def solve() -> int:
    file = open("input.txt", "r")
    grid: List[List[int]] = [
        [int(c) for c in line.strip()] for line in file.readlines()
    ]
    visible_trees = 0
    for (y, row) in enumerate(grid):
        for (x, _) in enumerate(row):
            if x == 0 or x == len(grid) - 1:
                visible_trees += 1
            elif y == 0 or y == len(grid) - 1:
                visible_trees += 1
            elif is_tree_visible(grid=grid, position=(x, y)):
                visible_trees += 1

    return visible_trees


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
