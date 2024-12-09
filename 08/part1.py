from collections import defaultdict
from itertools import combinations


def parse_input(path: str) -> dict[complex, str]:
    with open(path, "r") as input:
        return {
            complex(row_ix, col_ix): char
            for row_ix, row in enumerate(input)
            for col_ix, char in enumerate(row.strip())
        }


def solve(input: dict[complex, str]) -> int:
    char_to_coords = defaultdict(list)
    locations: set[complex] = set()
    for k, v in input.items():
        if v != ".":
            char_to_coords[v].append(k)
    for _, coords in char_to_coords.items():
        if len(coords) > 1:
            coord_pairs = list(combinations(coords, 2))
            for first_coord, second_coord in coord_pairs:
                first_antinode = first_coord - (second_coord - first_coord)
                second_antinode = second_coord + (second_coord - first_coord)
                if input.get(first_antinode):
                    locations.add(first_antinode)
                if input.get(second_antinode):
                    locations.add(second_antinode)
    return len(locations)


if __name__ == "__main__":
    assert solve(parse_input("./08/test")) == 14
    print(solve(parse_input("./08/input")))
