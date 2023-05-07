from typing import List, Tuple, Optional


def compare_elements(left_item: List, right_item: List) -> Optional[bool]:
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
                return None
            else:
                return left_item < right_item


def compare_lists(left: List, right: List) -> Optional[bool]:
    if len(left) == 0 and len(right) == 0:
        return None
    if len(left) == 0:
        return True
    if len(right) == 0:
        return False
    left_item = left.pop(0)
    right_item = right.pop(0)
    result = compare_elements(left_item, right_item)
    if result != None:
        return result
    return compare_lists(left, right)


def solve() -> int:
    input = open("input.txt", "r")

    pairs: List[Tuple[List, List]] = []
    current_pair_element: Optional[List] = None
    for line in [l.strip() for l in input.readlines()]:
        if line == "":
            continue
        if current_pair_element != None:
            pair = (current_pair_element, eval(line))
            pairs.append(pair)
            current_pair_element = None
        else:
            current_pair_element = eval(line)

    right_order_indices: List[int] = []
    for pair_index, (left, right) in enumerate(pairs):
        if compare_lists(left, right):
            right_order_indices.append(pair_index + 1)

    return sum(right_order_indices)


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
