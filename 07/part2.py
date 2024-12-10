def parse_input(path: str) -> list[tuple[int, list[int]]]:  # expected_result , numbers
    with open(path, "r") as input:
        parsed: list[int, list[int]] = list()
        for line in input.read().splitlines():
            split_line = line.split(":")
            parsed.append((int(split_line[0]), [int(x) for x in split_line[1].split()]))
        return parsed


def solve(input: list[tuple[int, list[int]]]) -> int:
    total = 0
    for target, numbers in input:
        current = numbers[0]
        correct = dfs(target, current, numbers[1:])
        if correct:
            total += target
    return total


def dfs(target: int, current: int, numbers: list[int]) -> bool:
    if len(numbers) > 0:
        return (
            dfs(target, current * numbers[0], numbers[1:])
            or dfs(target, current + numbers[0], numbers[1:])
            or dfs(target, int(f"{current}{numbers[0]}"), numbers[1:])
        )
    return True if current == target else False


if __name__ == "__main__":
    assert solve(parse_input("./07/test")) == 11387
    print(solve(parse_input("./07/input")))
