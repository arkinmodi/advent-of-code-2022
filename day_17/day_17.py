from __future__ import annotations

import argparse
import os.path
from copy import deepcopy

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_TXT = os.path.join(os.path.dirname(__file__), 'example.txt')


def day_17_part_1(filename: str) -> int:
    with open(filename) as f:
        input = [n.strip() for n in f]
    input = list(input[0])

    chamber: list[list[str]] = []
    jet = 0

    STARTING_SPACE = (
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.'],
    )

    STARTING_ROCKS = (
        (
            ['.', '.', '@', '@', '@', '@', '.'],
        ),
        (
            ['.', '.', '.', '@', '.', '.', '.'],
            ['.', '.', '@', '@', '@', '.', '.'],
            ['.', '.', '.', '@', '.', '.', '.'],
        ),
        (
            ['.', '.', '@', '@', '@', '.', '.'],
            ['.', '.', '.', '.', '@', '.', '.'],
            ['.', '.', '.', '.', '@', '.', '.'],
        ),
        (
            ['.', '.', '@', '.', '.', '.', '.'],
            ['.', '.', '@', '.', '.', '.', '.'],
            ['.', '.', '@', '.', '.', '.', '.'],
            ['.', '.', '@', '.', '.', '.', '.'],
        ),
        (
            ['.', '.', '@', '@', '.', '.', '.'],
            ['.', '.', '@', '@', '.', '.', '.'],
        ),
    )

    def can_move_down(rock_bottom: int, rock_height: int) -> bool:
        if rock_bottom <= 0:
            return False

        for r in range(rock_bottom, rock_bottom + rock_height):
            for c in range(len(chamber[0])):
                if chamber[r][c] == '@' and chamber[r - 1][c] == '#':
                    return False
        return True

    def can_move_left(rock_bottom: int, rock_height: int) -> bool:
        for r in range(rock_bottom, rock_bottom + rock_height):
            for c in range(len(chamber[0])):
                if (
                    chamber[r][c] == '@' and
                    (c <= 0 or chamber[r][c - 1] == '#')
                ):
                    return False
        return True

    def can_move_right(rock_bottom: int, rock_height: int) -> bool:
        for r in range(rock_bottom, rock_bottom + rock_height):
            for c in range(len(chamber[0])):
                if (
                    chamber[r][c] == '@' and
                    (c >= len(chamber[0]) - 1 or chamber[r][c + 1] == '#')
                ):
                    return False
        return True

    for rock in range(2022):
        # step 1: insert new rock
        chamber.extend(deepcopy(STARTING_SPACE))
        chamber.extend(deepcopy(STARTING_ROCKS[rock % len(STARTING_ROCKS)]))

        rock_height = len(STARTING_ROCKS[rock % len(STARTING_ROCKS)])
        rock_bottom = len(chamber) - rock_height

        is_falling = True
        while is_falling:

            # step 2: move rock with jet
            if input[jet] == '<' and can_move_left(rock_bottom, rock_height):
                for r in range(rock_bottom, rock_bottom + rock_height):
                    for c in range(1, len(chamber[0])):
                        if chamber[r][c] == '@':
                            chamber[r][c] = '.'
                            chamber[r][c - 1] = '@'
            elif (
                input[jet] == '>' and
                can_move_right(rock_bottom, rock_height)
            ):
                for r in range(rock_bottom, rock_bottom + rock_height):
                    for c in range(len(chamber[0]) - 2, -1, -1):
                        if chamber[r][c] == '@':
                            chamber[r][c] = '.'
                            chamber[r][c + 1] = '@'
            jet = (jet + 1) % len(input)

            # step 3: move rock down
            if not can_move_down(rock_bottom, rock_height):
                for r in range(rock_bottom, rock_bottom + rock_height):
                    for c in range(len(chamber[0])):
                        if chamber[r][c] == '@':
                            chamber[r][c] = '#'
                is_falling = False
            else:
                for r in range(rock_bottom, rock_bottom + rock_height):
                    for c in range(len(chamber[0])):
                        if chamber[r][c] == '@':
                            chamber[r][c] = '.'
                            chamber[r - 1][c] = '@'
                rock_bottom -= 1

        # step 4: remove excess rows (above highest_rock)
        while chamber[-1] == ['.', '.', '.', '.', '.', '.', '.']:
            chamber.pop()

    return len(chamber)


def _print_chamber(chamber: list[list[str]], num_rows: int) -> None:
    print()
    for i in range(len(chamber) - 1, max(len(chamber) - num_rows - 1, -1), -1):
        # print(f'{i + 1:05d}', ''.join(chamber[i]))
        print(''.join(chamber[i]))
    print()


def day_17_part_2(filename: str) -> int:
    with open(filename) as f:
        input = [n.strip() for n in f]
    input = list(input[0])

    return 0


@pytest.mark.parametrize(
    ('filename', 'expected'),
    (
        (EXAMPLE_TXT, 3068),
        (INPUT_TXT, 3133),
    ),
)
def test_day_17_part_1(filename: str, expected: int) -> None:
    assert day_17_part_1(filename) == expected


@pytest.mark.parametrize(
    ('filename', 'expected'),
    (
        (EXAMPLE_TXT, 1514285714288),
        # (INPUT_TXT, 209914),
    ),
)
def test_day_17_part_2(filename: str, expected: int) -> None:
    assert day_17_part_2(filename) == expected


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    print(f'Day 17 Part 1: {day_17_part_1(args.filename)}')
    print(f'Day 17 Part 2: {day_17_part_2(args.filename)}')
