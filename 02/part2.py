def parse_input(path: str) -> list[str]:
    with open(path, "r") as input:
        return input.read().splitlines()


def is_ascending_report(report: list[int]) -> bool:
    return all(1 <= (report[i + 1] - report[i]) <= 3 for i in range(len(report) - 1))


def is_descending_report(report: list[int]) -> bool:
    return all(1 <= (report[i] - report[i + 1]) <= 3 for i in range(len(report) - 1))


def is_valid_report(report: list[int]) -> bool:
    is_ascending = is_ascending_report(report)
    is_descending = is_descending_report(report)
    if is_ascending or is_descending:
        return True
    is_ascending_with_one_fixable_mistake = any(
        is_ascending_report(report[:i] + report[i + 1 :]) for i in range(len(report))
    )
    is_descending_with_one_fixable_mistake = any(
        is_descending_report(report[:i] + report[i + 1 :]) for i in range(len(report))
    )
    return (
        is_ascending_with_one_fixable_mistake or is_descending_with_one_fixable_mistake
    )


def solve(input: list[str]) -> int:
    reports = [list(map(int, line.split())) for line in input]
    return sum(is_valid_report(report) for report in reports)


if __name__ == "__main__":
    assert solve(parse_input("./02/test")) == 4
    print(solve(parse_input("./02/input")))
