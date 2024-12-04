from itertools import islice
from collections import deque
from typing import Generator, Iterable


def parse_input(path: str) -> list[str]:
    with open(path, "r") as input:
        return input.read().splitlines()


# https://docs.python.org/3/library/itertools.html#itertools-recipes
def sliding_window(iterable: Iterable[str], n: int) -> Generator[str, None, None]:
    iterator = iter(iterable)
    window = deque(islice(iterator, n - 1), maxlen=n)
    for item in iterator:
        window.append(item)
        yield "".join(window)


# https://stackoverflow.com/a/23069625
def get_diagonals(input: list[str]) -> list[str]:
    width = len(input[0])
    length = len(input)
    diagonals = []
    for diagonal_index in range(length + width - 1):
        diagonals.append(
            "".join(
                input[length - diagonal_index + i - 1][i]
                for i in range(
                    max(diagonal_index - length + 1, 0), min(diagonal_index + 1, width)
                )
            )
        )
        diagonals.append(
            "".join(
                input[diagonal_index - i][i]
                for i in range(
                    max(diagonal_index - length + 1, 0), min(diagonal_index + 1, width)
                )
            )
        )
    return diagonals


def solve(input: str) -> int:
    diagonals = get_diagonals(input)
    left_right = sum(
        1
        for line in input
        for window in sliding_window(line, 4)
        if window == "XMAS" or window == "SAMX"
    )
    flipped_list = list("".join(line) for line in zip(*input))
    top_down = sum(
        1
        for line in flipped_list
        for window in sliding_window(line, 4)
        if window == "XMAS" or window == "SAMX"
    )
    diagonal_count = sum(
        1
        for diagonal in diagonals
        for window in sliding_window(diagonal, 4)
        if window == "XMAS" or window == "SAMX"
    )
    return left_right + top_down + diagonal_count


if __name__ == "__main__":
    assert solve(parse_input("./04/test")) == 18
    print(solve(parse_input("./04/input")))
