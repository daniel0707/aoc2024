from itertools import islice, chain
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


def is_valid_box(box: list[str]) -> bool:
    return (
        box[0][0] == "M"
        and box[0][2] == "M"
        and box[1][1] == "A"
        and box[2][0] == "S"
        and box[2][2] == "S"
    )


def solve(input: str) -> int:
    length = len(input)
    three_by_three_boxes = list(
        chain.from_iterable(
            zip(
                sliding_window(input[i], 3),
                sliding_window(input[i + 1], 3),
                sliding_window(input[i + 2], 3),
            )
            for i in range(length - 2)
        )
    )

    boxes_with_rotations = [
        [
            box,
            box[::-1],
            tuple("".join(chars) for chars in (zip(*box))),
            tuple("".join(chars) for chars in (zip(*box)))[::-1],
        ]
        for box in three_by_three_boxes
    ]
    return sum(
        1 for boxes in boxes_with_rotations if any(is_valid_box(box) for box in boxes)
    )


if __name__ == "__main__":
    assert solve(parse_input("./04/test")) == 9
    print(solve(parse_input("./04/input")))
