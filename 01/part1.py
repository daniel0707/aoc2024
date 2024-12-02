def parse_input(path: str) -> list[str]:
    with open(path, "r") as input:
        return input.read().splitlines()


def solve(input: list[str]) -> int:
    left_list, right_list = [], []
    for line in input:
        left, right = [int(x) for x in line.split()]
        left_list.append(left)
        right_list.append(right)

    left_list.sort()
    right_list.sort()
    tuple_list = zip(left_list, right_list)
    return sum([abs(a - b) for (a, b) in tuple_list])


def solve_one_liner(filename: str) -> int:
    return sum(
        abs(left - right)
        for left, right in zip(
            *map(
                sorted, zip(*[list(map(int, line.split())) for line in open(filename)])
            )
        )
    )


if __name__ == "__main__":
    assert solve(parse_input("./01/test")) == 11
    assert solve_one_liner("./01/test") == 11
    print(solve(parse_input("./01/input")))
    print(solve_one_liner("./01/input"))
