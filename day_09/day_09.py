from __future__ import annotations

import argparse
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_TXT_1 = os.path.join(os.path.dirname(__file__), 'example_1.txt')
EXAMPLE_TXT_2 = os.path.join(os.path.dirname(__file__), 'example_2.txt')


def day_09_part_1(filename: str) -> int:
    with open(filename) as f:
        input = [l.strip('\n') for l in f]

    head_x, head_y = 0, 0
    tail_x, tail_y = 0, 0
    tail_visited = {(tail_x, tail_y)}

    for command in input:
        direction, steps = command.split(' ')

        for _ in range(int(steps)):
            prev_head_x, prev_head_y = head_x, head_y

            # Update head
            match direction:
                case 'U': head_y += 1
                case 'D': head_y -= 1
                case 'R': head_x += 1
                case 'L': head_x -= 1
                case _: raise Exception('Invalid direction')

            # Check if tail is still touching head
            is_tail_valid = False
            for dx, dy in [(0, 0), (1, 0), (0, 1), (-1, 0), (0, -1), (1, 1), (-1, -1), (-1, 1), (1, -1)]:
                if tail_x + dx == head_x and tail_y + dy == head_y:
                    is_tail_valid = True
                    break

            # Update tail
            if not is_tail_valid:
                tail_x, tail_y = prev_head_x, prev_head_y
            tail_visited.add((tail_x, tail_y))

    return len(tail_visited)


def day_09_part_2(filename: str) -> int:
    with open(filename) as f:
        input = [l.strip('\n') for l in f]

    knots = [[0, 0] for _ in range(10)]
    knots_visited = [{(knots[0][0], knots[0][1])} for _ in range(10)]

    for command in input:
        direction, steps = command.split(' ')

        for _ in range(int(steps)):
            # Update head
            match direction:
                case 'U': knots[0][1] += 1
                case 'D': knots[0][1] -= 1
                case 'R': knots[0][0] += 1
                case 'L': knots[0][0] -= 1
                case _: raise Exception('Invalid direction')

            knots_visited[0].add((knots[0][0], knots[0][1]))

            for i in range(len(knots) - 1):
                dx = knots[i][0] - knots[i + 1][0]
                dy = knots[i][1] - knots[i + 1][1]

                if abs(dx) > 1:
                    knots[i + 1][0] += 1 if dx > 0 else -1
                    if abs(dy) != 0:
                        knots[i + 1][1] += 1 if dy > 0 else -1
                elif abs(dy) > 1:
                    knots[i + 1][1] += 1 if dy > 0 else -1
                    if abs(dx) != 0:
                        knots[i + 1][0] += 1 if dx > 0 else -1

                knots_visited[i + 1].add((knots[i + 1][0], knots[i + 1][1]))

    return len(knots_visited[-1])


@pytest.mark.parametrize(
    ('filename', 'expected'),
    (
        (EXAMPLE_TXT_1, 13),
        (INPUT_TXT, 6745),
    ),
)
def test_day_09_part_1(filename: str, expected: int) -> None:
    assert day_09_part_1(filename) == expected


@pytest.mark.parametrize(
    ('filename', 'expected'),
    (
        (EXAMPLE_TXT_1, 1),
        (EXAMPLE_TXT_2, 36),
        (INPUT_TXT, 2793),
    ),
)
def test_day_09_part_2(filename: str, expected: int) -> None:
    assert day_09_part_2(filename) == expected


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    print(f"Day 9 Part 1: {day_09_part_1(args.filename)}")
    print(f"Day 9 Part 2: {day_09_part_2(args.filename)}")
