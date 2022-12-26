from typing import List


def tick(register: int, buffer: str) -> str:
    index = len(buffer)
    if index >= register - 1 and index <= register + 1:
        buffer += "#"
    else:
        buffer += "."
    if len(buffer) == 40:
        print(buffer)
        buffer = ""
    return buffer


def solve() -> None:
    file = open("input.txt", "r")
    instructions = [line.strip() for line in file.readlines()]
    register = 1
    buffer = ""
    buffer = tick(register=register, buffer=buffer)
    for instruction in instructions:
        if instruction.startswith("addx"):
            operand = int(instruction.split()[-1])
            buffer = tick(register=register, buffer=buffer)
            register += operand
            buffer = tick(register=register, buffer=buffer)
        elif instruction.startswith("noop"):
            buffer = tick(register=register, buffer=buffer)
    return


def main() -> None:
    solve()


if __name__ == "__main__":
    main()
