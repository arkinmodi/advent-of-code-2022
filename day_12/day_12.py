import argparse
import collections
import math
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_TXT = os.path.join(os.path.dirname(__file__), 'example.txt')


def day_12_part_1(filename: str) -> int:
    with open(filename) as f:
        input = [l.strip() for l in f]

    # Build Height Map
    height_map = [list(line) for line in input]
    ROW, COL = len(height_map), len(height_map[0])

    # Find Start point
    START = (0, 0)
    for i, r in enumerate(height_map):
        for j, c in enumerate(r):
            if c == 'S':
                START = (i, j)
                break

    def is_scalable(src: tuple[int, int], dest: tuple[int, int]) -> bool:
        def to_int_height(c: str) -> int:
            match c:
                case 'S': return ord('a')
                case 'E': return ord('z')
                case _: return ord(c)

        src_height = to_int_height(height_map[src[0]][src[1]])
        dest_height = to_int_height(height_map[dest[0]][dest[1]])
        return dest_height - src_height <= 1

    # BFS
    queue = collections.deque([START])
    visited = set([START])
    steps = 0
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            curr_r, curr_c = queue.popleft()

            if height_map[curr_r][curr_c] == 'E':
                return steps

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_r = curr_r + dr
                new_c = curr_c + dc

                if (
                    (new_r, new_c) not in visited and
                    0 <= new_r < ROW and
                    0 <= new_c < COL and
                    is_scalable((curr_r, curr_c), (new_r, new_c))
                ):
                    queue.append((new_r, new_c))
                    visited.add((new_r, new_c))
        steps += 1
    return -1


def day_12_part_2(filename: str) -> int:
    with open(filename) as f:
        input = [l.strip() for l in f]

    # Build Height Map
    height_map = [list(line) for line in input]
    ROW, COL = len(height_map), len(height_map[0])

    # Find End point
    END = (0, 0)
    for i, r in enumerate(height_map):
        for j, c in enumerate(r):
            if c == 'E':
                END = (i, j)
                break

    def is_scalable(src: tuple[int, int], dest: tuple[int, int]) -> bool:
        def to_int_height(c: str) -> int:
            match c:
                case 'S': return ord('a')
                case 'E': return ord('z')
                case _: return ord(c)

        src_height = to_int_height(height_map[src[0]][src[1]])
        dest_height = to_int_height(height_map[dest[0]][dest[1]])
        return dest_height - src_height <= 1

    # BFS
    queue = collections.deque([END])
    visited = set([END])
    steps = 0
    while queue:
        level_size = len(queue)
        for i in range(level_size):
            curr_r, curr_c = queue.popleft()

            if (
                height_map[curr_r][curr_c] == 'S' or
                height_map[curr_r][curr_c] == 'a'
            ):
                return steps

            for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                new_r = curr_r + dr
                new_c = curr_c + dc

                if (
                    (new_r, new_c) not in visited and
                    0 <= new_r < ROW and
                    0 <= new_c < COL and
                    is_scalable((new_r, new_c), (curr_r, curr_c))
                ):
                    queue.append((new_r, new_c))
                    visited.add((new_r, new_c))
        steps += 1
    return -1


@pytest.mark.parametrize(
    ("filename", "expected"),
    (
        (EXAMPLE_TXT, 31),
        (INPUT_TXT, 447),
    )
)
def test_day_12_part_1(filename: str, expected: int) -> None:
    assert day_12_part_1(filename) == expected


@pytest.mark.parametrize(
    ("filename", "expected"),
    (
        (EXAMPLE_TXT, 29),
        (INPUT_TXT, 446),
    )
)
def test_day_12_part_2(filename: str, expected: int) -> None:
    assert day_12_part_2(filename) == expected


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    print(f"Day 12 Part 1: {day_12_part_1(args.filename)}")
    print(f"Day 12 Part 2: {day_12_part_2(args.filename)}")
