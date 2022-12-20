from __future__ import annotations
from typing import Optional, Dict, List
from dataclasses import dataclass, field


@dataclass
class Directory:
    identifier: str
    parent: Optional[Directory] = None
    dirs: Dict[str, Directory] = field(default_factory=dict)
    files: Dict[str, int] = field(default_factory=dict)


def calculate_size(directory: Directory) -> int:
    total_size = sum(directory.files.values())
    for (_, dir) in directory.dirs.items():
        total_size += calculate_size(directory=dir)
    return total_size


def solve() -> int:
    file = open("input.txt", "r")

    directories: List = []

    root_id = file.readline().strip().split()[-1]
    root: Directory = Directory(identifier=root_id)
    directories.append(root)
    current_node: Directory = root
    reading_output = False
    while True:
        line = file.readline().strip()
        if line == "":
            break
        if reading_output == True:
            if not line.startswith("$"):
                if line.startswith("dir"):
                    identifier = line.split()[-1]
                    node = Directory(identifier=identifier, parent=current_node)
                    current_node.dirs[identifier] = node
                    directories.append(node)
                else:
                    (size, file_name) = tuple(line.split())
                    current_node.files[file_name] = int(size)
                continue
            else:
                reading_output = False

        if line.startswith("$ ls"):
            reading_output = True
        elif line.startswith("$ cd "):
            if ".." in line:
                current_node = current_node.parent
            else:
                identifier = line.split()[-1]
                current_node = current_node.dirs[identifier]

    result = 0
    for directory in directories:
        directory_size = calculate_size(directory=directory)
        if directory_size <= 100000:
            result += directory_size

    return result


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
