def parse_input(path: str) -> list[str]:
    with open(path, "r") as input:
        return input.read().splitlines()


def is_valid_report(report: list[int]) -> bool:
    is_ascending = all(
        1 <= (report[i + 1] - report[i]) <= 3 for i in range(len(report) - 1)
    )
    is_descending = all(
        1 <= (report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1)
    )
    return is_ascending or is_descending


def solve(input: list[str]) -> int:
    reports = [list(map(int, line.split())) for line in input]
    return sum(is_valid_report(report) for report in reports)


if __name__ == "__main__":
    assert solve(parse_input("./02/test")) == 2
    print(solve(parse_input("./02/input")))
