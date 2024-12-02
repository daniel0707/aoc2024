from itertools import pairwise


def parse_input(path: str) -> list[str]:
    with open(path, "r") as input:
        return input.read().splitlines()


def is_ascending_report(report: list[int]) -> bool:
    return all(1 <= (b - a) <= 3 for a, b in pairwise(report))


def is_descending_report(report: list[int]) -> bool:
    return all(1 <= (a - b) <= 3 for a, b in pairwise(report))


def is_valid_report(report: list[int]) -> bool:
    return any(
        is_ascending_report(report[:i] + report[i + 1 :])
        or is_descending_report(report[:i] + report[i + 1 :])
        for i in range(len(report))
    )


def solve(input: list[str]) -> int:
    reports = [list(map(int, line.split())) for line in input]
    return sum(is_valid_report(report) for report in reports)


if __name__ == "__main__":
    assert solve(parse_input("./02/test")) == 4
    print(solve(parse_input("./02/input")))
