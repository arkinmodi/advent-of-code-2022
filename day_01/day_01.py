import argparse
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_TXT = os.path.join(os.path.dirname(__file__), 'example.txt')


def day_01_part_1(filename: str) -> int:
    with open(filename) as f:
        input = [n.strip() for n in f]

    elf_calories = []
    curr = 0
    for food in input:
        if food:
            curr += int(food)
        else:
            elf_calories.append(curr)
            curr = 0
    elf_calories.append(curr)

    return max(elf_calories)


def day_01_part_2(filename: str) -> int:
    with open(filename) as f:
        input = [n.strip() for n in f]

    elf_calories = []
    curr = 0
    for food in input:
        if food:
            curr += int(food)
        else:
            elf_calories.append(curr)
            curr = 0
    elf_calories.append(curr)

    elf_calories.sort(reverse=True)
    return sum(elf_calories[:3])


@pytest.mark.parametrize(
    ("filename", "expected"),
    (
        (EXAMPLE_TXT, 24000),
    )
)
def test_day_01_part_1(filename: str, expected: int) -> None:
    assert day_01_part_1(filename) == expected


@pytest.mark.parametrize(
    ("filename", "expected"),
    (
        (EXAMPLE_TXT, 45000),
    )
)
def test_day_01_part_2(filename: str, expected: int) -> None:
    assert day_01_part_2(filename) == expected


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    print(f"Day 1 Part 1: {day_01_part_1(args.filename)}")
    print(f"Day 1 Part 2: {day_01_part_2(args.filename)}")
