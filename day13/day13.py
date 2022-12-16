from itertools import zip_longest
from functools import cmp_to_key


# Inspired by https://github.com/Praful/advent_of_code/blob/main/2022/src/day13.py


def parse_input(path="day13_input.txt"):
    with open(path) as f:
        lines = f.read().splitlines()

    pairs = []
    for i, line in enumerate(lines):
        if i % 3 == 0:
            pairs.append((eval(lines[i]), eval(lines[i+1])))
    return pairs


def compare(left, right):
    if left is None:
        return -1
    if right is None:
        return 1

    if isinstance(left, int) and isinstance(right, int):
        return -1 if left < right else (1 if left > right else 0)
    elif isinstance(left, list) and isinstance(right, list):
        for left_val, right_val in zip_longest(left, right):
            outcome = compare(left_val, right_val)
            if outcome != 0:
                return outcome
        return 0
    else:
        left = [left] if isinstance(left, int) else left
        right = [right] if isinstance(right, int) else right
        return compare(left, right)


def part1():
    pairs = parse_input()
    in_order = set()
    for i, pair in enumerate(pairs):
        left, right = pair
        if compare(left, right) == -1:
            in_order.add(i+1)
    print(sum(in_order))


def part2():
    pairs = parse_input()
    packets = []
    for left, right in pairs:
        packets.append(left)
        packets.append(right)
    sorted_packets = sorted([*packets, [[2]], [[6]]], key=cmp_to_key(compare))
    print((sorted_packets.index([[2]]) + 1) * (sorted_packets.index([[6]])+1))


if __name__ == "__main__":
    part1()
    part2()
