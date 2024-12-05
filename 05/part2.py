def parse_input(path: str) -> tuple[list[tuple[int, int]], list[list[int]]]:
    with open(path, "r") as input:
        page_rules, page_orders = input.read().split("\n\n")
        page_rules = [
            tuple(map(int, line.split("|"))) for line in page_rules.split("\n")
        ]
        page_orders = [
            list(map(int, line.split(","))) for line in page_orders.split("\n")
        ]
    return page_rules, page_orders


def solve(input: tuple[list[tuple[int, int]], list[list[int]]]) -> int:
    total = 0
    page_rules, page_orders = input

    page_rules_and_page_orders_to_fix = [
        (active_rules, page_order)
        for page_order in page_orders
        if (
            active_rules := [
                rule
                for rule in page_rules
                if rule[0] in page_order and rule[1] in page_order
            ]
        )
        and any(
            page_order.index(rule[0]) > page_order.index(rule[1])
            for rule in active_rules
        )
    ]

    for rules, page_order in page_rules_and_page_orders_to_fix:
        while any(
            page_order.index(rule[0]) > page_order.index(rule[1]) for rule in rules
        ):
            for rule in rules:
                if page_order.index(rule[0]) > page_order.index(rule[1]):
                    (
                        page_order[page_order.index(rule[0])],
                        page_order[page_order.index(rule[1])],
                    ) = (
                        page_order[page_order.index(rule[1])],
                        page_order[page_order.index(rule[0])],
                    )
        total += page_order[len(page_order) // 2]

    return total


if __name__ == "__main__":
    assert solve(parse_input("./05/test")) == 123
    print(solve(parse_input("./05/input")))
