from itertools import zip_longest
from collections import deque


def parse_input(path: str) -> str:
    with open(path, "r") as input:
        return input.read().strip()


def solve(input: str) -> int:
    # (ID, (block, free))
    files = list(
        enumerate(
            zip_longest(
                list(map(int, input[::2])), list(map(int, input[1::2])), fillvalue=0
            )
        )
    )
    total = 0
    file_queue = deque(files)
    free_spaces: list[tuple[int, int]] = []  # (start_index, length)
    pointer = 0

    for file in files:
        pointer += file[1][0]
        if file[1][1] > 0:
            free_spaces.append((pointer, file[1][1]))
        pointer += file[1][1]

    while len(file_queue) > 0:
        file_index, (block_amount, _) = file_queue.pop()
        before = sum([blocks + space for _, (blocks, space) in list(file_queue)])
        fit = next((space for space in free_spaces if space[1] >= block_amount), None)
        if fit is not None and fit[0] < before:
            if fit[1] > block_amount:
                free_spaces[free_spaces.index(fit)] = (
                    fit[0] + block_amount,
                    fit[1] - block_amount,
                )
            else:
                free_spaces.remove(fit)
            for pos in range(fit[0], fit[0] + block_amount):
                total += file_index * pos
            free_spaces.append((before, block_amount))
            free_spaces.sort(key=lambda x: x[0])
        else:
            for pos in range(before, before + block_amount):
                total += pos * file_index
    return total


if __name__ == "__main__":
    assert solve(parse_input("./09/test")) == 2858
    print(solve(parse_input("./09/input")))
