from __future__ import annotations

import argparse
import collections
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_TXT = os.path.join(os.path.dirname(__file__), 'example.txt')


def day_16_part_1(filename: str) -> int:
    with open(filename) as f:
        input = [line.strip() for line in f]

    tunnels = collections.defaultdict(list)
    valves = {}  # how much pressure the room's valve will release

    for line in input:
        line_list = line.split()
        room_id = line_list[1]
        flow_rate = line_list[4]
        neighbours = line_list[9:]

        valves[room_id] = int(flow_rate.split('=')[-1][:-1])
        for nei in neighbours:
            if nei[-1] == ',':
                tunnels[room_id].append(nei[:-1])
            else:
                tunnels[room_id].append(nei)

    dists = {}
    nonempty = []

    for valve in valves:
        if valve != 'AA' and not valves[valve]:
            continue

        if valve != 'AA':
            nonempty.append(valve)

        dists[valve] = {valve: 0, 'AA': 0}
        visited = {valve}
        queue = collections.deque([(0, valve)])

        while queue:
            dist, pos = queue.popleft()
            for nei in tunnels[pos]:
                if nei not in visited:
                    visited.add(nei)
                    if valves[nei]:
                        dists[valve][nei] = dist + 1
                    queue.append((dist + 1, nei))

        del dists[valve][valve]
        if valve != 'AA':
            del dists[valve]['AA']

    indices = {}
    for i, el in enumerate(nonempty):
        indices[el] = i

    cache: dict[tuple[int, str, int], int] = {}

    def dfs(time: int, valve: str, bitmask: int) -> int:
        if (time, valve, bitmask) in cache:
            return cache[(time, valve, bitmask)]

        max_valve = 0

        for nei in dists[valve]:
            bit = 1 << indices[nei]
            if bitmask & bit:
                continue

            remaining_time = time - dists[valve][nei] - 1
            if remaining_time <= 0:
                continue

            max_valve = max(
                max_valve,
                dfs(remaining_time, nei, bitmask | bit) +
                valves[nei] * remaining_time,
            )

        cache[(time, valve, bitmask)] = max_valve
        return max_valve

    return dfs(30, 'AA', 0)


def day_16_part_2(filename: str) -> int:
    with open(filename) as f:
        input = [line.strip() for line in f]

    tunnels = collections.defaultdict(list)
    valves = {}  # how much pressure the room's valve will release

    for line in input:
        line_list = line.split()
        room_id = line_list[1]
        flow_rate = line_list[4]
        neighbours = line_list[9:]

        valves[room_id] = int(flow_rate.split('=')[-1][:-1])
        for nei in neighbours:
            if nei[-1] == ',':
                tunnels[room_id].append(nei[:-1])
            else:
                tunnels[room_id].append(nei)

    dists = {}
    nonempty = []

    for valve in valves:
        if valve != 'AA' and not valves[valve]:
            continue

        if valve != 'AA':
            nonempty.append(valve)

        dists[valve] = {valve: 0, 'AA': 0}
        visited = {valve}
        queue = collections.deque([(0, valve)])

        while queue:
            dist, pos = queue.popleft()
            for nei in tunnels[pos]:
                if nei not in visited:
                    visited.add(nei)
                    if valves[nei]:
                        dists[valve][nei] = dist + 1
                    queue.append((dist + 1, nei))

        del dists[valve][valve]
        if valve != 'AA':
            del dists[valve]['AA']

    indices = {}
    for i, el in enumerate(nonempty):
        indices[el] = i

    cache: dict[tuple[int, str, int], int] = {}

    def dfs(time: int, valve: str, bitmask: int) -> int:
        if (time, valve, bitmask) in cache:
            return cache[(time, valve, bitmask)]

        max_valve = 0

        for nei in dists[valve]:
            bit = 1 << indices[nei]
            if bitmask & bit:
                continue

            remaining_time = time - dists[valve][nei] - 1
            if remaining_time <= 0:
                continue

            max_valve = max(
                max_valve,
                dfs(remaining_time, nei, bitmask | bit) +
                valves[nei] * remaining_time,
            )

        cache[(time, valve, bitmask)] = max_valve
        return max_valve

    max_pressure_release = 0
    b = (1 << len(nonempty)) - 1

    for i in range((b + 1) // 2):
        max_pressure_release = max(
            max_pressure_release,
            dfs(26, 'AA', i) + dfs(26, 'AA', b ^ i),
        )

    return max_pressure_release


@pytest.mark.parametrize(
    ('filename', 'expected'),
    (
        (EXAMPLE_TXT, 1651),
        (INPUT_TXT, 2114),
    ),
)
def test_day_16_part_1(filename: str, expected: int) -> None:
    assert day_16_part_1(filename) == expected


@pytest.mark.parametrize(
    ('filename', 'expected'),
    (
        (EXAMPLE_TXT, 1707),
        # (INPUT_TXT, 2666),
    ),
)
def test_day_16_part_2(filename: str, expected: int) -> None:
    assert day_16_part_2(filename) == expected


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    print(f'Day 16 Part 1: {day_16_part_1(args.filename)}')
    print(f'Day 16 Part 2: {day_16_part_2(args.filename)}')
