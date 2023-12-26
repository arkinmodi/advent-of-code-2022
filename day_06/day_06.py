from __future__ import annotations

import argparse
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_TXT_1 = os.path.join(os.path.dirname(__file__), 'example_1.txt')
EXAMPLE_TXT_2 = os.path.join(os.path.dirname(__file__), 'example_2.txt')
EXAMPLE_TXT_3 = os.path.join(os.path.dirname(__file__), 'example_3.txt')
EXAMPLE_TXT_4 = os.path.join(os.path.dirname(__file__), 'example_4.txt')
EXAMPLE_TXT_5 = os.path.join(os.path.dirname(__file__), 'example_5.txt')


def day_06_part_1(filename: str) -> int:
    with open(filename) as f:
        input = f.read().splitlines()

    data_stream = input[0]
    for i in range(len(data_stream) - 3):
        if len(set(data_stream[i:i+4])) == 4:
            return i + 4

    return -1


def day_06_part_2(filename: str) -> int:
    with open(filename) as f:
        input = f.read().splitlines()

    data_stream = input[0]
    for i in range(len(data_stream) - 13):
        if len(set(data_stream[i:i+14])) == 14:
            return i + 14

    return -1


@pytest.mark.parametrize(
    ('filename', 'expected'),
    (
        (EXAMPLE_TXT_1, 7),
        (EXAMPLE_TXT_2, 5),
        (EXAMPLE_TXT_3, 6),
        (EXAMPLE_TXT_4, 10),
        (EXAMPLE_TXT_5, 11),
        (INPUT_TXT, 1275),
    ),
)
def test_day_06_part_1(filename: str, expected: int) -> None:
    assert day_06_part_1(filename) == expected


@pytest.mark.parametrize(
    ('filename', 'expected'),
    (
        (EXAMPLE_TXT_1, 19),
        (EXAMPLE_TXT_2, 23),
        (EXAMPLE_TXT_3, 23),
        (EXAMPLE_TXT_4, 29),
        (EXAMPLE_TXT_5, 26),
        (INPUT_TXT, 3605),
    ),
)
def test_day_06_part_2(filename: str, expected: int) -> None:
    assert day_06_part_2(filename) == expected


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    print(f"Day 6 Part 1: {day_06_part_1(args.filename)}")
    print(f"Day 6 Part 2: {day_06_part_2(args.filename)}")
