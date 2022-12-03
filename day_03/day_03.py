import argparse
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_TXT = os.path.join(os.path.dirname(__file__), 'example.txt')


def day_03_part_1(filename: str) -> int:
    with open(filename) as f:
        input = [l.strip() for l in f]

    common = []
    for rucksack in input:
        first_compartment = rucksack[:len(rucksack) // 2]
        second_compartment = rucksack[len(rucksack) // 2:]
        common.extend(set(first_compartment) & set(second_compartment))

    def priority(c: str) -> int:
        if c.islower():
            return ord(c) - 96
        else:
            return ord(c) - 38

    return sum([priority(c) for c in common])


def day_03_part_2(filename: str) -> int:
    with open(filename) as f:
        input = [l.strip() for l in f]

    common = []
    for i in range(0, len(input) - 2, 3):
        common.extend(set(input[i]) & set(input[i + 1]) & set(input[i + 2]))

    def priority(c: str) -> int:
        if c.islower():
            return ord(c) - 96
        else:
            return ord(c) - 38

    return sum([priority(c) for c in common])


@pytest.mark.parametrize(
    ("filename", "expected"),
    (
        (EXAMPLE_TXT, 157),
    )
)
def test_day_03_part_1(filename: str, expected: int) -> None:
    assert day_03_part_1(filename) == expected


@pytest.mark.parametrize(
    ("filename", "expected"),
    (
        (EXAMPLE_TXT, 70),
    )
)
def test_day_03_part_2(filename: str, expected: int) -> None:
    assert day_03_part_2(filename) == expected


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    print(f"Day 3 Part 1: {day_03_part_1(args.filename)}")
    print(f"Day 3 Part 2: {day_03_part_2(args.filename)}")
