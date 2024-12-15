import re


def parse_input(path: str):
    with open(path, "r") as input:
        return [[*map(int, re.findall(r"-?\d+", line))] for line in input.readlines()]


def solve(input: list[tuple[int, int, int, int]], width: int, height: int) -> int:
    q1, q2, q3, q4 = 0, 0, 0, 0
    for robot in input:
        pos_x, pos_y, speed_x, speed_y = robot
        final_x = (pos_x + speed_x * 100) % width
        final_y = (pos_y + speed_y * 100) % height
        if final_x < width // 2 and final_y < height // 2:
            q1 += 1
        if final_x > width // 2 and final_y < height // 2:
            q2 += 1
        if final_x < width // 2 and final_y > height // 2:
            q3 += 1
        if final_x > width // 2 and final_y > height // 2:
            q4 += 1
    return q1 * q2 * q3 * q4


if __name__ == "__main__":
    assert solve(parse_input("./14/test"), 11, 7) == 12
    print(solve(parse_input("./14/input"), 101, 103))
