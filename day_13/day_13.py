from __future__ import annotations

import argparse
import functools
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_TXT = os.path.join(os.path.dirname(__file__), 'example.txt')


def day_13_part_1(filename: str) -> int:
    with open(filename) as f:
        input = [line.strip() for line in f if line.strip() != '']

    # 1 = Right Order, -1 = Not Right Order, 0 = Ran Out Of Items
    def is_right_order(left: list, right: list) -> int:

        for i in range(len(left)):
            if i == len(right):
                return -1

            left_type = type(left[i])
            right_type = type(right[i])
            order = 0

            if left_type == int and right_type == int:
                if left[i] > right[i]:
                    return -1
                elif left[i] < right[i]:
                    return 1

            elif left_type == list and right_type == list:
                order = is_right_order(left[i], right[i])

            elif left_type == int and right_type == list:
                order = is_right_order([left[i]], right[i])

            elif left_type == list and right_type == int:
                order = is_right_order(left[i], [right[i]])

            if order != 0:
                return order

        if len(left) < len(right):
            return 1
        return 0

    right_order_idx: list[int] = []
    id = 1
    for i in range(0, len(input) - 1, 2):
        left = eval(input[i])
        right = eval(input[i + 1])
        if is_right_order(left, right) != -1:
            right_order_idx.append(id)
        id += 1

    return sum(right_order_idx)


def day_13_part_2(filename: str) -> int:
    with open(filename) as f:
        input = [eval(line.strip()) for line in f if line.strip() != '']
    input.append([[2]])
    input.append([[6]])

    # 1 = Right Order, -1 = Not Right Order, 0 = Ran Out Of Items
    def is_right_order(left: list, right: list) -> int:

        for i in range(len(left)):
            if i == len(right):
                return -1

            left_type = type(left[i])
            right_type = type(right[i])
            order = 0

            if left_type == int and right_type == int:
                if left[i] > right[i]:
                    return -1
                elif left[i] < right[i]:
                    return 1

            elif left_type == list and right_type == list:
                order = is_right_order(left[i], right[i])

            elif left_type == int and right_type == list:
                order = is_right_order([left[i]], right[i])

            elif left_type == list and right_type == int:
                order = is_right_order(left[i], [right[i]])

            if order != 0:
                return order

        if len(left) < len(right):
            return 1
        return 0

    input.sort(reverse=True, key=functools.cmp_to_key(is_right_order))
    return (input.index([[2]]) + 1) * (input.index([[6]]) + 1)


@pytest.mark.parametrize(
    ('filename', 'expected'),
    (
        (EXAMPLE_TXT, 13),
        (INPUT_TXT, 5659),
    ),
)
def test_day_13_part_1(filename: str, expected: int) -> None:
    assert day_13_part_1(filename) == expected


@pytest.mark.parametrize(
    ('filename', 'expected'),
    (
        (EXAMPLE_TXT, 140),
        (INPUT_TXT, 22110),
    ),
)
def test_day_13_part_2(filename: str, expected: int) -> None:
    assert day_13_part_2(filename) == expected


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    print(f"Day 13 Part 1: {day_13_part_1(args.filename)}")
    print(f"Day 13 Part 2: {day_13_part_2(args.filename)}")
