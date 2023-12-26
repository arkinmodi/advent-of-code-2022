from __future__ import annotations

import argparse
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_TXT = os.path.join(os.path.dirname(__file__), 'example.txt')


def day_07_part_1(filename: str) -> int:
    with open(filename) as f:
        input = f.read().splitlines()

    class Folder:
        def __init__(self, size: int = 0, name: str = '', parent=None) -> None:
            self.size = size
            self.name = name
            self.parent = parent
            self.children: list[Folder] = []

        def index_of_folder(self, target: str) -> int:
            for i, f in enumerate(self.children):
                if f.name == target:
                    return i
            return -1

        def get_size(self) -> int:
            size = self.size
            for f in self.children:
                size += f.get_size()
            return size

        def print_tree(self) -> None:
            print(
                f"name: {self.name} \t size: {self.get_size()} \t children: {
                    [c.name for c in self.children]
                }",
            )
            for f in self.children:
                f.print_tree()

    root = Folder(name='/')
    curr_folder = root

    # Build Folder Structure
    for line in input:
        output = line.split(' ')
        if output[0] == '$' and output[1] == 'cd':
            if output[2] == '/':
                curr_folder = root
            elif output[2] == '..':
                curr_folder = curr_folder.parent
            else:
                folder_index = curr_folder.index_of_folder(output[2])
                if folder_index != -1:
                    curr_folder = curr_folder.children[folder_index]
                else:
                    new_folder = Folder(
                        name=output[2],
                        parent=curr_folder,
                    )
                    curr_folder.children.append(new_folder)
                    curr_folder = new_folder
        elif output[0].isdigit():
            curr_folder.size += int(output[0])

    stack = [root]
    total_size = 0
    while stack:
        curr = stack.pop()
        curr_size = curr.get_size()
        total_size += curr_size if curr_size <= 100000 else 0
        for c in curr.children:
            stack.append(c)

    return total_size


def day_07_part_2(filename: str) -> int:
    with open(filename) as f:
        input = f.read().splitlines()

    class Folder:
        def __init__(self, size: int = 0, name: str = '', parent=None) -> None:
            self.size = size
            self.name = name
            self.parent = parent
            self.children: list[Folder] = []

        def index_of_folder(self, target: str) -> int:
            for i, f in enumerate(self.children):
                if f.name == target:
                    return i
            return -1

        def get_size(self) -> int:
            size = self.size
            for f in self.children:
                size += f.get_size()
            return size

        def print_tree(self) -> None:
            print(
                f"name: {self.name} \t size: {self.get_size()} \t children: {
                    [c.name for c in self.children]
                }",
            )
            for f in self.children:
                f.print_tree()

    root = Folder(name='/')
    curr_folder = root

    # Build Folder Structure
    for line in input:
        output = line.split(' ')
        if output[0] == '$':
            if output[1] == 'cd':
                if output[2] == '/':
                    curr_folder = root
                elif output[2] == '..':
                    curr_folder = curr_folder.parent
                else:
                    folder_index = curr_folder.index_of_folder(output[2])
                    if folder_index != -1:
                        curr_folder = curr_folder.children[folder_index]
                    else:
                        new_folder = Folder(
                            name=output[2],
                            parent=curr_folder,
                        )
                        curr_folder.children.append(new_folder)
                        curr_folder = new_folder
        elif output[0].isdigit():
            curr_folder.size += int(output[0])

    TOTAL_SPACE = 70000000
    MIN_SPACE_NEEDED = 30000000

    folder_sizes = []
    stack = [root]
    while stack:
        curr = stack.pop()
        folder_sizes.append((curr.name, curr.get_size()))
        for c in curr.children:
            stack.append(c)

    folder_sizes.sort(key=lambda x: x[1])
    TOTAL_USED_SPACE = folder_sizes[-1][1]

    if TOTAL_USED_SPACE <= TOTAL_SPACE - MIN_SPACE_NEEDED:
        return 0

    # Binary Search
    left, right = 0, len(folder_sizes)  # [left, right)
    while left < right:
        mid = left + (right - left) // 2
        if (
            TOTAL_USED_SPACE -
            folder_sizes[mid][1] <= TOTAL_SPACE - MIN_SPACE_NEEDED
        ):
            right = mid
        else:
            left = mid + 1

    return folder_sizes[left][1]


@pytest.mark.parametrize(
    ('filename', 'expected'),
    (
        (EXAMPLE_TXT, 95437),
        (INPUT_TXT, 1118405),
    ),
)
def test_day_07_part_1(filename: str, expected: int) -> None:
    assert day_07_part_1(filename) == expected


@pytest.mark.parametrize(
    ('filename', 'expected'),
    (
        (EXAMPLE_TXT, 24933642),
        (INPUT_TXT, 12545514),
    ),
)
def test_day_07_part_2(filename: str, expected: int) -> None:
    assert day_07_part_2(filename) == expected


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    print(f"Day 7 Part 1: {day_07_part_1(args.filename)}")
    print(f"Day 7 Part 2: {day_07_part_2(args.filename)}")
