from collections import defaultdict
from itertools import combinations
import math


def parse_input(path: str) -> dict[complex, str]:
    with open(path, "r") as input:
        return {
            complex(row_ix, col_ix): char
            for row_ix, row in enumerate(input)
            for col_ix, char in enumerate(row.strip())
        }


def solve(input: dict[complex, str]) -> int:
    char_to_coords = defaultdict(list[complex])
    locations: set[complex] = set()
    for k, v in input.items():
        if v != ".":
            char_to_coords[v].append(k)
    for _, coords in char_to_coords.items():
        if len(coords) > 1:
            coord_pairs = list(combinations(coords, 2))
            for first_coord, second_coord in coord_pairs:
                locations.add(first_coord)
                locations.add(second_coord)
                diff = second_coord - first_coord
                gcd = math.gcd(int(diff.real), int(diff.imag))
                vector = complex(int(diff.real / gcd), int(diff.imag / gcd))
                next_pos = first_coord - vector
                while input.get(next_pos):
                    locations.add(next_pos)
                    next_pos -= vector
                next_pos = first_coord + vector
                while input.get(next_pos):
                    locations.add(next_pos)
                    next_pos += vector
    return len(locations)


if __name__ == "__main__":
    assert solve(parse_input("./08/test")) == 34
    print(solve(parse_input("./08/input")))
