from collections import deque
import re


def parse_input(path: str):
    with open(path, "r") as input:
        return [[*map(int, re.findall(r"-?\d+", line))] for line in input.readlines()]


def bfs(pos: complex, positions: set[complex], visited: set[complex]) -> list[complex]:
    visited.add(pos)
    queue = deque([pos])
    group: list[complex] = []
    while queue:
        current = queue.popleft()
        group.append(current)
        for direction in [1, -1, 1j, -1j]:
            new_pos = current + direction
            if new_pos in positions and new_pos not in visited:
                visited.add(new_pos)
                queue.append(new_pos)
    return group


def get_distinct_groups(positions: list[complex]) -> list[list[complex]]:
    positions_set = set(positions)
    visited = set()
    groups = []
    for pos in positions:
        if pos not in visited:
            groups.append(bfs(pos, positions_set, visited))
    return groups


def solve(input: list[tuple[int, int, int, int]], width: int, height: int) -> int:
    seconds = 1
    while True:
        positions: set[complex] = set()
        for robot in input:
            pos_x, pos_y, speed_x, speed_y = robot
            final_x = (pos_x + speed_x * seconds) % width
            final_y = (pos_y + speed_y * seconds) % height
            positions.add(complex(final_x, final_y))
        groups = get_distinct_groups(positions)
        if any(len(group) > 30 for group in groups):
            return seconds
        seconds += 1


if __name__ == "__main__":
    print(solve(parse_input("./14/input"), 101, 103))
