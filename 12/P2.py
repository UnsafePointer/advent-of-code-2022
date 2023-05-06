from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict, Tuple, Set
from sys import maxsize
from collections import defaultdict
from heapq import heappush, heappop


@dataclass
class Node:
    identifier: Tuple[int, int]
    height_data: str
    adjacent_nodes: List[Node] = field(default_factory=list)

    def __hash__(self) -> int:
        return hash(self.identifier)

    def __lt__(self, other: Node) -> bool:
        return self.identifier < other.identifier

    def height(self) -> int:
        if self.height_data == "S":
            return ord("a")
        elif self.height_data == "E":
            return ord("z")
        else:
            return ord(self.height_data)


def solve() -> int:
    input = open("input.txt", "r")
    data: List[List[str]] = []
    for line in input.readlines():
        data.append([c for c in line.strip()])

    nodes: Dict[Tuple[int, int], Node] = {}
    start_node: Node
    end_node: Node
    for row_index, row in enumerate(data):
        for column_index, c in enumerate(row):
            current_node: Node
            if (row_index, column_index) not in nodes:
                current_node = Node(identifier=(row_index, column_index), height_data=c)
            else:
                current_node = nodes[(row_index, column_index)]

            if c == "S":
                start_node = current_node
            elif c == "E":
                end_node = current_node

            adjacent_node: Node
            if column_index > 0:  # left
                position = (row_index, column_index - 1)
                if position not in nodes:
                    adjacent_node = Node(
                        identifier=(row_index, column_index),
                        height_data=data[row_index][column_index - 1],
                    )
                    nodes[position] = adjacent_node
                else:
                    adjacent_node = nodes[position]
                current_node.adjacent_nodes.append(adjacent_node)

            if column_index < len(data[row_index]) - 1:  # right
                position = (row_index, column_index + 1)
                if position not in nodes:
                    adjacent_node = Node(
                        identifier=(row_index, column_index),
                        height_data=data[row_index][column_index + 1],
                    )
                    nodes[position] = adjacent_node
                else:
                    adjacent_node = nodes[position]
                current_node.adjacent_nodes.append(adjacent_node)

            if row_index > 0:  # up
                position = (row_index - 1, column_index)
                if position not in nodes:
                    adjacent_node = Node(
                        identifier=(row_index, column_index),
                        height_data=data[row_index - 1][column_index],
                    )
                    nodes[position] = adjacent_node
                else:
                    adjacent_node = nodes[position]
                current_node.adjacent_nodes.append(adjacent_node)

            if row_index < len(data) - 1:  # down
                position = (row_index + 1, column_index)
                if position not in nodes:
                    adjacent_node = Node(
                        identifier=(row_index, column_index),
                        height_data=data[row_index + 1][column_index],
                    )
                    nodes[position] = adjacent_node
                else:
                    adjacent_node = nodes[position]
                current_node.adjacent_nodes.append(adjacent_node)

    visited: Set[Node] = set()
    distances: Dict[Node, int] = defaultdict(lambda: maxsize)
    distances[start_node] = 0

    priority_queue: List[Tuple[int, Node]] = []
    heappush(priority_queue, (0, start_node))
    while priority_queue:
        while True:
            (_, current_node) = heappop(priority_queue)
            if current_node not in visited:
                break

        for adjacent_node in current_node.adjacent_nodes:
            if adjacent_node.height() > current_node.height() + 1:
                continue

            adjacent_node_distance = distances[current_node] + (
                0 if adjacent_node.height_data == "a" else 1
            )
            if adjacent_node_distance < distances[adjacent_node]:
                distances[adjacent_node] = adjacent_node_distance
                heappush(priority_queue, (adjacent_node_distance, adjacent_node))
        visited.add(current_node)

    return distances[end_node]


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
