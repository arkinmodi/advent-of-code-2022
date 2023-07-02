import argparse
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_TXT_1 = os.path.join(os.path.dirname(__file__), 'example_1.txt')
EXAMPLE_TXT_2 = os.path.join(os.path.dirname(__file__), 'example_2.txt')


def day_10_part_1(filename: str) -> int:
    with open(filename) as f:
        input = [l.strip('\n') for l in f]

    x, signal_strength, cycle = 1, 0, 0
    tasks = []
    line = 0
    while line < len(input) or len(tasks) != 0:
        cycle += 1

        # Update existing tasks
        i = 0
        while i < len(tasks):
            tasks[i][1] -= 1
            if tasks[i][1] == 0:
                x += (tasks.pop(i))[0]
            else:
                i += 1

        # Add new task
        if line < len(input) and len(tasks) == 0:
            cmd = input[line].split(' ')
            if cmd[0] == "addx":
                tasks.append([int(cmd[1]), 2])
            line += 1

        # Update signal strength
        if cycle % 40 == 20:
            signal_strength += cycle * x

    return signal_strength


def day_10_part_2(filename: str) -> str:
    with open(filename) as f:
        input = [l.strip('\n') for l in f]

    SCREEN_WIDTH, SCREEN_HEIGHT = 40, 6
    crt_screen = ""

    x, tasks, line = 1, [], 0
    for cycle in range(SCREEN_WIDTH * SCREEN_HEIGHT):

        # Update existing tasks
        i = 0
        while i < len(tasks):
            tasks[i][1] -= 1
            if tasks[i][1] == 0:
                x += (tasks.pop(i))[0]
            else:
                i += 1

        # Add new task
        if line < len(input) and len(tasks) == 0:
            cmd = input[line].split(' ')
            if cmd[0] == "addx":
                tasks.append([int(cmd[1]), 2])
            line += 1

        # Update screen
        if cycle % 40 == 0:
            crt_screen += '\n'

        if (
            cycle % SCREEN_WIDTH == x or
            cycle % SCREEN_WIDTH == x - 1 or
            cycle % SCREEN_WIDTH == x + 1
        ):
            crt_screen += '#'
        else:
            crt_screen += '.'

    return crt_screen + '\n'


@pytest.mark.parametrize(
    ("filename", "expected"),
    (
        (EXAMPLE_TXT_1, 0),
        (EXAMPLE_TXT_2, 13140),
        (INPUT_TXT, 11960),
    ),
)
def test_day_10_part_1(filename: str, expected: int) -> None:
    assert day_10_part_1(filename) == expected


EXAMPLE_TXT_2_PART_2_EXPECTED = """
##..##..##..##..##..##..##..##..##..##..
###...###...###...###...###...###...###.
####....####....####....####....####....
#####.....#####.....#####.....#####.....
######......######......######......####
#######.......#######.......#######.....
"""

INPUT_TXT_2_PART_2_EXPECTED = """
####...##..##..####.###...##..#....#..#.
#.......#.#..#.#....#..#.#..#.#....#..#.
###.....#.#....###..#..#.#....#....####.
#.......#.#....#....###..#.##.#....#..#.
#....#..#.#..#.#....#....#..#.#....#..#.
####..##...##..#....#.....###.####.#..#.
"""


@pytest.mark.parametrize(
    ("filename", "expected"),
    (
        (EXAMPLE_TXT_2, EXAMPLE_TXT_2_PART_2_EXPECTED),
        (INPUT_TXT, INPUT_TXT_2_PART_2_EXPECTED),
    ),
)
def test_day_10_part_2(filename: str, expected: str) -> None:
    assert day_10_part_2(filename) == expected


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    print(f"Day 10 Part 1: {day_10_part_1(args.filename)}")
    print(f"Day 10 Part 2:\n{day_10_part_2(args.filename)}")
