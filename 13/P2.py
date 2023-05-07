from typing import List, Tuple, Optional
from functools import cmp_to_key
from copy import deepcopy


def compare_elements(left_item: List, right_item: List) -> int:
    if type(left_item) != type(right_item):
        if type(left_item) != list:
            return compare_lists([left_item], right_item)
        else:
            return compare_lists(left_item, [right_item])
    else:
        if type(left_item) == list:
            return compare_lists(left_item, right_item)
        else:
            if left_item == right_item:
                return 0
            else:
                return 1 if left_item < right_item else -1


def compare_lists(left: List, right: List) -> int:
    if len(left) == 0 and len(right) == 0:
        return 0
    if len(left) == 0:
        return 1
    if len(right) == 0:
        return -1
    left_item = left.pop(0)
    right_item = right.pop(0)
    result = compare_elements(left_item, right_item)
    if result != 0:
        return result
    return compare_lists(left, right)


def compare(left: List, right: List) -> int:
    left_clone = deepcopy(left)
    right_clone = deepcopy(right)
    return compare_lists(left_clone, right_clone)


def solve() -> int:
    input = open("input.txt", "r")

    packets: List = []
    for line in [l.strip() for l in input.readlines()]:
        if line == "":
            continue
        packets.append(eval(line))

    first_divider_packet = [[2]]
    packets.append(first_divider_packet)
    second_divider_packet = [[6]]
    packets.append(second_divider_packet)

    compare_key = cmp_to_key(compare)
    packets.sort(key=compare_key, reverse=True)

    return (packets.index(first_divider_packet) + 1) * (
        packets.index(second_divider_packet) + 1
    )


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
