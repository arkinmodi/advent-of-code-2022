import argparse
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_TXT = os.path.join(os.path.dirname(__file__), 'example.txt')


def day_14_part_1(filename: str) -> int:
    with open(filename) as f:
        input = [l.strip() for l in f]

    SAND_SOURCE = (500, 0)
    LOWEST_ROCK = 0

    rocks: set[tuple[int, int]] = set()
    resting_sand: set[tuple[int, int]] = set()

    # Build Rocks
    for line in input:
        points = line.split(' -> ')
        for i in range(len(points) - 1):
            x1_str, y1_str = points[i].split(',')
            x2_str, y2_str = points[i + 1].split(',')

            x1, y1 = int(x1_str), int(y1_str)
            x2, y2 = int(x2_str), int(y2_str)

            LOWEST_ROCK = max(LOWEST_ROCK, y1, y2)

            if abs(x2 - x1) == 0:
                start = min(y1, y2)
                end = max(y1, y2)
                for y in range(start, end + 1):
                    rocks.add((x1, y))
            else:
                start = min(x1, x2)
                end = max(x1, x2)
                for x in range(start, end + 1):
                    rocks.add((x, y1))

    # Drop Sand
    active_sand = list(SAND_SOURCE)
    while active_sand[1] < LOWEST_ROCK:
        if (
            (active_sand[0], active_sand[1] + 1) not in rocks and
            (active_sand[0], active_sand[1] + 1) not in resting_sand
        ):
            active_sand[1] += 1

        elif (
            (active_sand[0] - 1, active_sand[1] + 1) not in rocks and
            (active_sand[0] - 1, active_sand[1] + 1) not in resting_sand
        ):
            active_sand[0] -= 1
            active_sand[1] += 1

        elif (
            (active_sand[0] + 1, active_sand[1] + 1) not in rocks and
            (active_sand[0] + 1, active_sand[1] + 1) not in resting_sand
        ):
            active_sand[0] += 1
            active_sand[1] += 1

        else:
            resting_sand.add(tuple(active_sand))
            active_sand = list(SAND_SOURCE)

    return len(resting_sand)


def day_14_part_2(filename: str) -> int:
    with open(filename) as f:
        input = [l.strip() for l in f]

    SAND_SOURCE = (500, 0)
    FLOOR = 0

    rocks: set[tuple[int, int]] = set()
    resting_sand: set[tuple[int, int]] = set()

    # Build Rocks
    for line in input:
        points = line.split(' -> ')
        for i in range(len(points) - 1):
            x1_str, y1_str = points[i].split(',')
            x2_str, y2_str = points[i + 1].split(',')

            x1, y1 = int(x1_str), int(y1_str)
            x2, y2 = int(x2_str), int(y2_str)

            FLOOR = max(FLOOR, y1, y2)

            if abs(x2 - x1) == 0:
                start = min(y1, y2)
                end = max(y1, y2)
                for y in range(start, end + 1):
                    rocks.add((x1, y))
            else:
                start = min(x1, x2)
                end = max(x1, x2)
                for x in range(start, end + 1):
                    rocks.add((x, y1))

    FLOOR += 2

    # Drop Sand
    active_sand = list(SAND_SOURCE)
    while SAND_SOURCE not in resting_sand:
        if (
            (active_sand[0], active_sand[1] + 1) not in rocks and
            (active_sand[0], active_sand[1] + 1) not in resting_sand and
            active_sand[1] + 1 != FLOOR
        ):
            active_sand[1] += 1

        elif (
            (active_sand[0] - 1, active_sand[1] + 1) not in rocks and
            (active_sand[0] - 1, active_sand[1] + 1) not in resting_sand and
            active_sand[1] + 1 != FLOOR
        ):
            active_sand[0] -= 1
            active_sand[1] += 1

        elif (
            (active_sand[0] + 1, active_sand[1] + 1) not in rocks and
            (active_sand[0] + 1, active_sand[1] + 1) not in resting_sand and
            active_sand[1] + 1 != FLOOR
        ):
            active_sand[0] += 1
            active_sand[1] += 1

        else:
            resting_sand.add(tuple(active_sand))
            active_sand = list(SAND_SOURCE)

    return len(resting_sand)


@pytest.mark.parametrize(
    ("filename", "expected"),
    (
        (EXAMPLE_TXT, 24),
        (INPUT_TXT, 763),
    )
)
def test_day_14_part_1(filename: str, expected: int) -> None:
    assert day_14_part_1(filename) == expected


@pytest.mark.parametrize(
    ("filename", "expected"),
    (
        (EXAMPLE_TXT, 93),
        (INPUT_TXT, 23921),
    )
)
def test_day_14_part_2(filename: str, expected: int) -> None:
    assert day_14_part_2(filename) == expected


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    print(f"Day 14 Part 1: {day_14_part_1(args.filename)}")
    print(f"Day 14 Part 2: {day_14_part_2(args.filename)}")
