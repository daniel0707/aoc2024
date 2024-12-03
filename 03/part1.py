import re


def parse_input(path: str) -> str:
    with open(path, "r") as input:
        return input.read().strip()


def solve(input: str) -> int:
    regex_mult = r"mul\((\d+),(\d+)\)"
    return sum(
        int(m.group(1)) * int(m.group(2))
        for m in re.finditer(regex_mult, input, re.DOTALL)
    )


if __name__ == "__main__":
    assert solve(parse_input("./03/test")) == 161
    print(solve(parse_input("./03/input")))
