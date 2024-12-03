import re


def parse_input(path: str) -> str:
    with open(path, "r") as input:
        return input.read().strip()


def solve(input: str) -> int:
    regex_mult = r"mul\((\d+),(\d+)\)"
    regex_skip = r"don't\(\).*?(?=don't\(\)|do\(\)|$)"

    input = re.sub(regex_skip, "", input, flags=re.DOTALL)

    return sum(
        int(m.group(1)) * int(m.group(2))
        for m in re.finditer(regex_mult, input, re.DOTALL)
    )


if __name__ == "__main__":
    assert solve(parse_input("./03/test")) == 48
    print(solve(parse_input("./03/input")))
