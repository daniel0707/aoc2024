def parse_input(path: str) -> dict[complex, int]:
    with open(path, "r") as input:
        return {
            complex(row_ix, col_ix): int(char)
            for row_ix, row in enumerate(input)
            for col_ix, char in enumerate(row.strip())
        }


def solve(input: dict[complex, int]) -> int:
    starters = [k for k, v in input.items() if v == 0]
    total = 0
    for starter in starters:
        visited = set([starter])
        total += dfs(input, starter, visited)
    return total


def dfs(input: dict[complex, int], current: complex, visited: set[complex]) -> int:
    directions: list[complex] = [1, -1, 1j, -1j]
    score = 0
    if input[current] == 9:
        return score + 1
    for direction in directions:
        new = current + direction
        if new not in visited and new in input and input[new] - input[current] == 1:
            visited.add(new)
            score += dfs(input, new, visited)
    return score


if __name__ == "__main__":
    assert solve(parse_input("./10/test")) == 36
    print(solve(parse_input("./10/input")))
