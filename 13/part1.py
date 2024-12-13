import re


def parse_input(
    path: str,
) -> list[list[tuple[int, int], tuple[int, int], tuple[int, int]]]:
    with open(path, "r") as input:
        machines = input.read().split("\n\n")
        print(machines)
        return [tuple(map(int, re.findall(r"\d+", line))) for line in machines]


def solve(input: list[list[tuple[int, int], tuple[int, int], tuple[int, int]]]) -> int:
    print(input)
    tokens = 0
    for machine in input:
        button_Ax, button_Ay, button_Bx, button_By, prize_x, prize_y = machine
        solution = next(
            (
                (ax, bx)
                for ax in range(101)
                for bx in range(101)
                if ax * button_Ax + bx * button_Bx == prize_x
                and ax * button_Ay + bx * button_By == prize_y
            ),
            None,
        )
        if solution:
            tokens += solution[0] * 3 + solution[1]
    return tokens


if __name__ == "__main__":
    assert solve(parse_input("./13/test")) == 480
    print(solve(parse_input("./13/input")))
