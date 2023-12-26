from __future__ import annotations

import argparse
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_TXT = os.path.join(os.path.dirname(__file__), 'example.txt')


def day_08_part_1(filename: str) -> int:
    with open(filename) as f:
        input = f.read().splitlines()

    # Build Grid
    grid: list[list[int]] = []
    for line in input:
        grid.append([])
        for col in line:
            grid[-1].append(int(col))

    def is_visible(grid: list[list[int]], row: int, col: int) -> bool:
        ROW, COL = len(grid), len(grid[0])
        tree = grid[row][col]
        max_tree = -1

        # Up
        for i in range(row - 1, -1, -1):
            max_tree = max(max_tree, grid[i][col])

        if max_tree < tree:
            return True
        max_tree = -1

        # Down
        for i in range(row + 1, ROW):
            max_tree = max(max_tree, grid[i][col])

        if max_tree < tree:
            return True
        max_tree = -1

        # Left
        for i in range(col - 1, -1, -1):
            max_tree = max(max_tree, grid[row][i])

        if max_tree < tree:
            return True
        max_tree = -1

        # Right
        for i in range(col + 1, COL):
            max_tree = max(max_tree, grid[row][i])

        return max_tree < tree

    visible_trees = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if is_visible(grid, r, c):
                visible_trees += 1

    return visible_trees


def day_08_part_2(filename: str) -> int:
    with open(filename) as f:
        input = f.read().splitlines()

    # Build Grid
    grid: list[list[int]] = []
    for line in input:
        grid.append([])
        for col in line:
            grid[-1].append(int(col))

    def get_scenic_score(grid: list[list[int]], row: int, col: int) -> int:
        ROW, COL = len(grid), len(grid[0])
        tree = grid[row][col]
        scenic_score = [0, 0, 0, 0]  # [up, down, left, right]

        # Up
        for i in range(row - 1, -1, -1):
            scenic_score[0] += 1
            if grid[i][col] >= tree:
                break

        # Down
        for i in range(row + 1, ROW):
            scenic_score[1] += 1
            if grid[i][col] >= tree:
                break

        # Left
        for i in range(col - 1, -1, -1):
            scenic_score[2] += 1
            if grid[row][i] >= tree:
                break

        # Right
        for i in range(col + 1, COL):
            scenic_score[3] += 1
            if grid[row][i] >= tree:
                break

        total_score = 1
        for s in scenic_score:
            total_score *= s
        return total_score

    scenic_scores = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            scenic_scores.append(get_scenic_score(grid, r, c))

    return max(scenic_scores)


@pytest.mark.parametrize(
    ('filename', 'expected'),
    (
        (EXAMPLE_TXT, 21),
        (INPUT_TXT, 1676),
    ),
)
def test_day_08_part_1(filename: str, expected: int) -> None:
    assert day_08_part_1(filename) == expected


@pytest.mark.parametrize(
    ('filename', 'expected'),
    (
        (EXAMPLE_TXT, 8),
        (INPUT_TXT, 313200),
    ),
)
def test_day_08_part_2(filename: str, expected: int) -> None:
    assert day_08_part_2(filename) == expected


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    print(f"Day 8 Part 1: {day_08_part_1(args.filename)}")
    print(f"Day 8 Part 2: {day_08_part_2(args.filename)}")
