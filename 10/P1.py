from typing import List

clock = [20, 60, 100, 140, 180, 220]


def tick(current_cycles: int, register: int, state: List[int]) -> int:
    future_cycles = current_cycles + 1
    if future_cycles in clock:
        state.append(register)
    return future_cycles


def solve() -> int:
    file = open("input.txt", "r")
    instructions = [line.strip() for line in file.readlines()]
    register = 1
    cycles = 1
    state: List[int] = []
    for instruction in instructions:
        if instruction.startswith("addx"):
            operand = int(instruction.split()[-1])
            cycles = tick(current_cycles=cycles, register=register, state=state)
            register += operand
            cycles = tick(current_cycles=cycles, register=register, state=state)
        elif instruction.startswith("noop"):
            cycles = tick(current_cycles=cycles, register=register, state=state)
    return sum(list(map(lambda s, c: s * c, state, clock)))


def main() -> None:
    print(solve())


if __name__ == "__main__":
    main()
