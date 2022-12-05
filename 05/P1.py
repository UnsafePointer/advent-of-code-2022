from os import fstat
from dataclasses import dataclass, field
from typing import Deque, DefaultDict
from collections import defaultdict, deque


@dataclass
class Stacks:
    s: DefaultDict[int, Deque[str]] = field(default_factory=lambda: defaultdict(deque))

    def insert(self, identifier: str, index: int) -> None:
        self.s[index].appendleft(identifier)


def solve() -> str:
    stacks: Stacks = Stacks()

    file = open("input.txt", "r")
    end_of_file = fstat(file.fileno()).st_size
    while file.tell() != end_of_file:
        line = file.readline()
        if "[" in line:
            for idx, c in enumerate(line):
                if c == "[":
                    index = int(idx / 4)
                    stacks.insert(identifier=line[idx + 1], index=index)
        elif "move" in line:
            parsed = line.split(" ")
            times = int(parsed[1])
            move_from = int(parsed[3]) - 1
            move_to = int(parsed[5]) - 1
            for _ in range(times):
                element = stacks.s[move_from].pop()
                stacks.s[move_to].append(element)
    result = ""
    for idx in range(len(stacks.s.keys())):
        result += stacks.s[idx].pop()
    return result


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
