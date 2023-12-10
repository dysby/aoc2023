import functools
import operator
import re
from io import TextIOBase
import string


def is_number(data, max_v, max_h, i, a, b, limit_a, limit_b):
    if (data[i][limit_a] != "." and a != limit_a) or (
        data[i][limit_b] != "." and b != limit_b
    ):
        return True
    for y in [max(i - 1, 0), min(max_v, i + 1)]:
        if y == i:
            continue
        for x in range(limit_a, limit_b + 1):
            if data[y][x] != ".":
                return True
    return False


def is_gear(data, max_v, max_h, i, a, b, limit_a, limit_b):
    if data[i][limit_a] == "*":
        return True, (i, limit_a)
    if data[i][limit_b] == "*":
        return True, (i, limit_b)

    for y in [max(i - 1, 0), min(max_v, i + 1)]:
        if y == i:
            continue
        for x in range(limit_a, limit_b + 1):
            if data[y][x] == "*":
                return True, (y, x)
    return False, (None, None)


def answer(input_file: TextIOBase):
    data = input_file.read().splitlines()

    max_v = len(data) - 1
    max_h = len(data[0]) - 1

    numbers = []
    gears = {}

    for i, line in enumerate(data):
        for m in re.finditer(r"\d+", line):
            number = int(m.group())
            a, b = m.span()
            b -= 1
            limit_a = max(0, a - 1)
            limit_b = min(max_h, b + 1)

            # part1
            if is_number(data, max_v, max_h, i, a, b, limit_a, limit_b):
                numbers.append(number)

            # part2
            is_g, gear_x_y = is_gear(data, max_v, max_h, i, a, b, limit_a, limit_b)
            if is_g:
                gears.setdefault(gear_x_y, []).append(number)

    part1 = sum(numbers)
    print(f"Day 1, part1 answer = {part1}")

    part2 = sum(
        [
            functools.reduce(operator.mul, gear_values)
            for _, gear_values in gears.items()
            if len(gear_values) == 2
        ]
    )
    print(f"Day 1, part2 answer = {part2}")
