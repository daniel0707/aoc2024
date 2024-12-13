import re


def parse_input(
    path: str,
) -> list[list[tuple[int, int], tuple[int, int], tuple[int, int]]]:
    with open(path, "r") as input:
        machines = input.read().split("\n\n")
        return [tuple(map(int, re.findall(r"\d+", line))) for line in machines]


def determinant(a: int, b: int, c: int, d: int) -> int:
    return a * d - b * c


def solve(input: list[list[tuple[int, int], tuple[int, int], tuple[int, int]]]) -> int:
    tokens = 0
    for machine in input:
        button_Ax, button_Ay, button_Bx, button_By, prize_x, prize_y = machine
        prize_x += 10000000000000
        prize_y += 10000000000000
        # button_Ax * A + button_Bx * B = prize_x
        # button_Ay * A + button_By * B = prize_y
        d = determinant(button_Ax, button_Bx, button_Ay, button_By)
        if d == 0:
            continue

        A = determinant(prize_x, button_Bx, prize_y, button_By) / d
        B = determinant(button_Ax, prize_x, button_Ay, prize_y) / d

        if A >= 0 and B >= 0 and A.is_integer() and B.is_integer():
            tokens += A * 3 + B

    return tokens


if __name__ == "__main__":
    print(solve(parse_input("./13/test")))
    print(solve(parse_input("./13/input")))
