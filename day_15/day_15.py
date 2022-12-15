import argparse
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_TXT = os.path.join(os.path.dirname(__file__), 'example.txt')


def day_15_part_1(filename: str, target_row: int) -> int:
    with open(filename) as f:
        input = [l.strip() for l in f]

    no_beacons: set[int] = set()
    for line in input:
        l = line.split(' ')
        sensor_x = int(l[2].replace("x=", '').replace(',', ''))
        sensor_y = int(l[3].replace("y=", '').replace(':', ''))
        beacon_x = int(l[8].replace("x=", '').replace(',', ''))
        beacon_y = int(l[9].replace("y=", ''))

        manhattan_distance = abs(sensor_x - beacon_x) + \
            abs(sensor_y - beacon_y)

        distance_to_target_row = abs(sensor_y - target_row)

        no_beacons.update(range(
            sensor_x - manhattan_distance + distance_to_target_row,
            sensor_x + manhattan_distance - distance_to_target_row
        ))

    return len(no_beacons)


def day_15_part_2(filename: str, max_bound: int) -> int:
    with open(filename) as f:
        input = [l.strip() for l in f]

    sensor_beacon: set[tuple[tuple[int, int], tuple[int, int]]] = set()
    for line in input:
        l = line.split(' ')
        sensor_x = int(l[2].replace("x=", '').replace(',', ''))
        sensor_y = int(l[3].replace("y=", '').replace(':', ''))
        beacon_x = int(l[8].replace("x=", '').replace(',', ''))
        beacon_y = int(l[9].replace("y=", ''))
        sensor_beacon.add(((sensor_x, sensor_y), (beacon_x, beacon_y)))

    def manhattan_distance(x0: int, y0: int, x1: int, y1: int) -> int:
        return abs(x0 - x1) + abs(y0 - y1)

    def is_covered_by_sensor(x: int, y: int) -> bool:
        for s, b in sensor_beacon:
            if manhattan_distance(s[0], s[1], x, y) <= manhattan_distance(s[0], s[1], b[0], b[1]):
                return True
        return False

    x, y = -1, -1
    seen: set[tuple[int, int]] = set()
    for s, b in sensor_beacon:
        dist = manhattan_distance(s[0], s[1], b[0], b[1])

        # manhattan distance is equal to the length of one side
        # (sensor area is a square)
        for i in range(dist):
            if (
                0 <= s[0] - dist + i - 1 <= max_bound and
                0 <= s[1] + i <= max_bound and
                (s[0] - dist + i - 1, s[1] + i) not in seen
            ):
                # NW side
                if not is_covered_by_sensor(s[0] - dist + i - 1, s[1] + i):
                    x = s[0] - dist + i - 1
                    y = s[1] + i
                    break
                else:
                    seen.add((s[0] - dist + i - 1, s[1] + i))

            if (
                0 <= s[0] - dist + i + 1 <= max_bound and
                0 <= s[1] - i <= max_bound and
                (s[0] - dist + i + 1, s[1] - i) not in seen
            ):
                # SW side
                if not is_covered_by_sensor(s[0] - dist + i + 1, s[1] - i):
                    x = s[0] - dist + i + 1
                    y = s[1] - i
                    break
                else:
                    seen.add((s[0] - dist + i + 1, s[1] - i))

            if (
                0 <= s[0] + i <= max_bound and
                0 <= s[1] - dist - i - 1 <= max_bound and
                (s[0] + i, s[1] - dist - i - 1) not in seen
            ):
                # NE side
                if not is_covered_by_sensor(s[0] + i, s[1] - dist - i - 1):
                    x = s[0] + i
                    y = s[1] - dist - i - 1
                    break
                else:
                    seen.add((s[0] + i, s[1] - dist - i - 1))

            if (
                0 <= s[0] - i <= max_bound and
                0 <= s[1] - dist + i + 1 <= max_bound and
                (s[0] - i,  s[1] - dist + i + 1) not in seen
            ):
                # NE side
                if not is_covered_by_sensor(s[0] - i,  s[1] - dist + i + 1):
                    x = s[0] + i
                    y = s[1] - dist - i - 1
                    break
                else:
                    seen.add((s[0] - i,  s[1] - dist + i + 1))

    return x * 4_000_000 + y


@pytest.mark.parametrize(
    ("filename", "target_row", "expected"),
    (
        (EXAMPLE_TXT, 10, 26),
        (INPUT_TXT, 2_000_000, 6425133),
    )
)
def test_day_15_part_1(filename: str, target_row: int, expected: int) -> None:
    assert day_15_part_1(filename, target_row) == expected


@pytest.mark.parametrize(
    ("filename", "max_bound", "expected"),
    (
        (EXAMPLE_TXT, 20, 56000011),
        # (INPUT_TXT, 4_000_000, 10996191429555), # Too Slow To Run
    )
)
def test_day_15_part_2(filename: str, max_bound: int, expected: int) -> None:
    assert day_15_part_2(filename, max_bound) == expected


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=INPUT_TXT)
    parser.add_argument('-p1', '--target-row', type=int, default=2_000_000)
    parser.add_argument('-p2', '--max-bound', type=int, default=4_000_000)
    args = parser.parse_args()

    print(f"Day 15 Part 1: {day_15_part_1(args.filename, args.target_row)}")
    print(f"Day 15 Part 2: {day_15_part_2(args.filename, args.max_bound)}")
