def parse_input(path: str) -> list[list[str]]:
    with open(path, "r") as input:
        return [list(line) for line in input.read().splitlines()]


def solve(input: list[list[str]]) -> int:
    right_turn = -1j
    direction = -1  # up
    visited = set()
    pos_y = input.index(next(filter(lambda row: "^" in row, input)))
    pos_x = input[pos_y].index("^")
    position = complex(pos_y, pos_x)
    while (0 <= position.real < len(input)) and (0 <= position.imag < len(input[0])):
        visited.add(position)
        next_position = position + direction
        try:
            if input[int(next_position.real)][int(next_position.imag)] == "#":
                direction *= right_turn
            else:
                position = next_position
        except IndexError:
            break
    return len(visited)


if __name__ == "__main__":
    assert solve(parse_input("./06/test")) == 41
    print(solve(parse_input("./06/input")))
