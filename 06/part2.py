from copy import deepcopy


def parse_input(path: str) -> list[list[str]]:
    with open(path, "r") as input:
        return [list(line) for line in input.read().splitlines()]


def solve(input: list[list[str]]) -> int:
    right_turn = -1j
    direction = -1  # up
    visited: set[tuple[complex, complex]] = set()
    start_y = input.index(next(filter(lambda row: "^" in row, input)))
    start_x = input[start_y].index("^")
    position = complex(start_y, start_x)
    while (0 <= position.real < len(input)) and (0 <= position.imag < len(input[0])):
        visited.add((position, direction))
        next_position = position + direction
        try:
            if input[int(next_position.real)][int(next_position.imag)] == "#":
                direction *= right_turn
            else:
                position = next_position
        except IndexError:
            break
    loop_spots = set()
    options = visited.copy()
    options.remove((complex(start_y, start_x), -1))
    for option in options:
        option_pos = option[0]
        new_input = deepcopy(input)
        new_input[int(option_pos.real)][int(option_pos.imag)] = "#"
        # reset
        position = complex(start_y, start_x)
        visited.clear()
        direction = -1  # up

        while (0 <= position.real < len(new_input)) and (
            0 <= position.imag < len(new_input[0])
        ):
            visited.add((position, direction))
            next_position = position + direction
            try:
                if new_input[int(next_position.real)][int(next_position.imag)] == "#":
                    direction *= right_turn
                else:
                    position = next_position
            except IndexError:
                break
            if (position, direction) in visited:
                loop_spots.add(option_pos)
                break
    return len(loop_spots)


if __name__ == "__main__":
    assert solve(parse_input("./06/test")) == 6
    print(solve(parse_input("./06/input")))
