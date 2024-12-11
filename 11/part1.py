from collections import deque


def parse_input(path: str) -> list[int]:
    with open(path, "r") as input:
        return [int(x) for x in input.read().strip().split()]


def solve(input: list[int]) -> int:
    line = deque(input)
    for _ in range(25):
        new_line = deque()
        while len(line) > 0:
            stone = line.popleft()
            if stone == 0:
                new_line.append(1)
                continue
            str_val = str(stone)
            if len(str_val) % 2 == 0:
                left, right = str_val[: len(str_val) // 2], str_val[len(str_val) // 2 :]
                new_line.append(int(left))
                new_line.append(int(right))
                continue
            new_line.append(stone * 2024)
        line = new_line
    return len(line)


if __name__ == "__main__":
    assert solve(parse_input("./11/test")) == 55312
    print(solve(parse_input("./11/input")))
