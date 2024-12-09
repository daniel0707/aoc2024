from itertools import zip_longest
from collections import deque


def parse_input(path: str) -> str:
    with open(path, "r") as input:
        return input.read().strip()


def solve(input: str) -> int:
    # (ID, (block, free))
    files = deque(
        enumerate(
            zip_longest(
                list(map(int, input[::2])), list(map(int, input[1::2])), fillvalue=0
            )
        )
    )
    total = 0
    pointer = 0
    while len(files) > 0:
        file_index, (block_amount, space_amount) = files.popleft()
        for _ in range(block_amount):
            total += file_index * pointer
            pointer += 1
        if space_amount > 0 and len(files) > 0:
            r_file_index, (r_block_amount, _) = files.pop()
            while space_amount > 0:
                if r_block_amount == 0 and len(files) > 0:
                    r_file_index, (r_block_amount, _) = files.pop()
                space_amount -= 1
                total += r_file_index * pointer
                pointer += 1
                r_block_amount -= 1
            if r_block_amount > 0:
                files.append((r_file_index, (r_block_amount, 0)))
    return total


if __name__ == "__main__":
    assert solve(parse_input("./09/test")) == 1928
    print(solve(parse_input("./09/input")))
