from collections import Counter
from functools import cache


def parse_input(path: str) -> dict[int, int]:  # stone writing, count of such stones
    with open(path, "r") as input:
        return Counter(int(x) for x in input.read().strip().split())


def solve(input: dict[int, int], blinks: int) -> int:
    line = input
    for ix in range(blinks):
        new_line = Counter()
        for stone, count in line.items():
            ixs = handle_stone(stone)
            for ix in ixs:
                new_line[ix] += count
        line = new_line
    return sum(line.values())


@cache
def handle_stone(stone: int) -> list[int]:
    if stone == 0:
        return [1]
    elif len(str_val := str(stone)) % 2 == 0:
        left, right = (
            int(str_val[: len(str_val) // 2]),
            int(str_val[len(str_val) // 2 :]),
        )
        return [left, right]
    else:
        return [stone * 2024]


if __name__ == "__main__":
    assert solve(parse_input("./11/test"), 25) == 55312
    print(solve(parse_input("./11/input"), 75))
