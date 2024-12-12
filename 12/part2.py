from string import ascii_uppercase
from collections import deque


def parse_input(path: str) -> dict[complex, str]:
    with open(path, "r") as input:
        return {
            complex(row_ix, col_ix): char
            for row_ix, row in enumerate(input)
            for col_ix, char in enumerate(row.strip())
        }


def solve(input: dict[complex, str]) -> int:
    letters_positions = get_letters_positions(input)
    letters_positions = [group for group in letters_positions if group]
    # list of groups of adjacent letters
    letters_groups: list[list[complex]] = [
        group
        for positions in letters_positions
        for group in get_distinct_groups(positions)
    ]
    return sum(get_border_sides(group) * len(group) for group in letters_groups)


def get_border_sides(group: list[complex]) -> int:
    edges_position_direction: set[complex, complex] = set()
    for pos in group:
        for direction in [1, -1, 1j, -1j]:
            if pos + direction not in group:
                edges_position_direction.add((pos, direction))
    return sum(
        1
        for pos, direction in edges_position_direction
        if (pos + direction * 1j, direction) not in edges_position_direction
    )


def get_letters_positions(input: dict[complex, str]) -> list[list[complex]]:
    return [
        [pos for pos, char in input.items() if char == letter]
        for letter in ascii_uppercase
    ]


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


if __name__ == "__main__":
    assert solve(parse_input("./12/test")) == 80
    print(solve(parse_input("./12/input")))
