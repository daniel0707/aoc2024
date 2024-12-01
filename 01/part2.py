from collections import Counter


def solve(filename: str)->int:
    left_list,right_list = zip(*[list(map(int, line.split())) for line in open(filename)])
    return sum([left_int * Counter(right_list)[left_int] for left_int in left_list])

if __name__ == "__main__":
    assert solve("./01/test") == 31
    print(solve("./01/input"))