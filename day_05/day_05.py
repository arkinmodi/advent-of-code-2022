import argparse
import collections
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_TXT = os.path.join(os.path.dirname(__file__), 'example.txt')


def day_05_part_1(filename: str) -> str:
    with open(filename) as f:
        input = [l.strip('\n') for l in f]

    NUM_OF_STACKS = 0
    BOTTOM_LAYER_INDEX = -1
    for i in range(len(input)):
        if input[i][1] == '1':
            NUM_OF_STACKS = int(input[i][-2])
            BOTTOM_LAYER_INDEX = i - 1
            break

    stacks = [[] for _ in range(NUM_OF_STACKS)]
    for i in range(BOTTOM_LAYER_INDEX, -1, -1):
        stack_idx = 1
        for j in range(len(stacks)):
            if input[i][stack_idx].isalpha():
                stacks[j].append(input[i][stack_idx])
            stack_idx += 4

    for i in range(BOTTOM_LAYER_INDEX + 3, len(input)):
        order = input[i].split(' ')
        quantity = int(order[1])
        from_stack = int(order[3]) - 1
        to_stack = int(order[5]) - 1

        for _ in range(quantity):
            stacks[to_stack].append(stacks[from_stack].pop())

    return "".join([s[-1] for s in stacks])


def day_05_part_2(filename: str) -> str:
    with open(filename) as f:
        input = [l.strip('\n') for l in f]

    NUM_OF_STACKS = 0
    BOTTOM_LAYER_INDEX = -1
    for i in range(len(input)):
        if input[i][1] == '1':
            NUM_OF_STACKS = int(input[i][-2])
            BOTTOM_LAYER_INDEX = i - 1
            break

    stacks = [[] for _ in range(NUM_OF_STACKS)]
    for i in range(BOTTOM_LAYER_INDEX, -1, -1):
        stack_idx = 1
        for j in range(len(stacks)):
            if input[i][stack_idx].isalpha():
                stacks[j].append(input[i][stack_idx])
            stack_idx += 4

    for i in range(BOTTOM_LAYER_INDEX + 3, len(input)):
        order = input[i].split(' ')
        quantity = int(order[1])
        from_stack = int(order[3]) - 1
        to_stack = int(order[5]) - 1

        crane = collections.deque()
        for _ in range(quantity):
            crane.appendleft(stacks[from_stack].pop())
        stacks[to_stack].extend(crane)

    return "".join([s[-1] for s in stacks])


@pytest.mark.parametrize(
    ("filename", "expected"),
    (
        (EXAMPLE_TXT, "CMZ"),
        (INPUT_TXT, "VGBBJCRMN"),
    )
)
def test_day_05_part_1(filename: str, expected: int) -> None:
    assert day_05_part_1(filename) == expected


@pytest.mark.parametrize(
    ("filename", "expected"),
    (
        (EXAMPLE_TXT, "MCD"),
        (INPUT_TXT, "LBBVJBRMH"),
    )
)
def test_day_05_part_2(filename: str, expected: int) -> None:
    assert day_05_part_2(filename) == expected


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    print(f"Day 5 Part 1: {day_05_part_1(args.filename)}")
    print(f"Day 5 Part 2: {day_05_part_2(args.filename)}")
