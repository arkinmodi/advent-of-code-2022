import argparse
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_TXT = os.path.join(os.path.dirname(__file__), 'example.txt')


def day_04_part_1(filename: str) -> int:
    with open(filename) as f:
        input = [l.strip() for l in f]

    overlap = 0
    for pair in input:
        first, second = pair.split(",")

        first_start, first_end = first.split("-")
        first_start, first_end = int(first_start), int(first_end)

        second_start, second_end = second.split("-")
        second_start, second_end = int(second_start), int(second_end)

        if (
            (first_start <= second_start and first_end >= second_end) or
            (first_start >= second_start and first_end <= second_end)
        ):
            overlap += 1

    return overlap


def day_04_part_2(filename: str) -> int:
    with open(filename) as f:
        input = [l.strip() for l in f]

    overlap = 0
    for pair in input:
        first, second = pair.split(",")

        first_start, first_end = first.split("-")
        first_start, first_end = int(first_start), int(first_end)

        second_start, second_end = second.split("-")
        second_start, second_end = int(second_start), int(second_end)

        if (
            (first_start <= second_start and first_end >= second_end) or
            (first_start >= second_start and first_end <= second_end) or
            (first_start >= second_start and first_start <= second_end) or
            (first_end >= second_start and first_end <= second_end)
        ):
            overlap += 1

    return overlap


@pytest.mark.parametrize(
    ("filename", "expected"),
    (
        (EXAMPLE_TXT, 2),
        (INPUT_TXT, 459),
    )
)
def test_day_04_part_1(filename: str, expected: int) -> None:
    assert day_04_part_1(filename) == expected


@pytest.mark.parametrize(
    ("filename", "expected"),
    (
        (EXAMPLE_TXT, 4),
        (INPUT_TXT, 779),
    )
)
def test_day_04_part_2(filename: str, expected: int) -> None:
    assert day_04_part_2(filename) == expected


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    print(f"Day 4 Part 1: {day_04_part_1(args.filename)}")
    print(f"Day 4 Part 2: {day_04_part_2(args.filename)}")
