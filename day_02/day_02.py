import argparse
import os.path

import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_TXT = os.path.join(os.path.dirname(__file__), 'example.txt')


def day_02_part_1(filename: str) -> int:
    with open(filename) as f:
        input = [n.strip() for n in f]

    def decrypt_opponent(move: str) -> str:
        match move:
            case 'A': return "rock"
            case 'B': return "paper"
            case 'C': return "scissors"
            case _: raise Exception("Invalid Move")

    def decrypt_me(move: str) -> str:
        match move:
            case 'X': return "rock"
            case 'Y': return "paper"
            case 'Z': return "scissors"
            case _: raise Exception("Invalid Move")

    total_score = 0
    for round in input:
        op_encrypted, my_encrypted = round.split(" ")
        op_move, my_move = decrypt_opponent(
            op_encrypted), decrypt_me(my_encrypted)

        score = 0
        if my_move == "rock":
            score = 1
        elif my_move == "paper":
            score = 2
        else:
            score = 3

        if my_move == op_move:
            score += 3
        elif (
            (my_move == "rock" and op_move == "scissors") or
            (my_move == "paper" and op_move == "rock") or
            (my_move == "scissors" and op_move == "paper")
        ):
            score += 6

        total_score += score

    return total_score


# def day_02_part_2(filename: str) -> int:
#     with open(filename) as f:
#         input = [n.strip() for n in f]

#     return 0


@pytest.mark.parametrize(
    ("filename", "expected"),
    (
        (EXAMPLE_TXT, 15),
    )
)
def test_day_02_part_1(filename: str, expected: int) -> None:
    assert day_02_part_1(filename) == expected


# @pytest.mark.parametrize(
#     ("filename", "expected"),
#     (
#         (EXAMPLE_TXT, 45000),
#     )
# )
# def test_day_02_part_2(filename: str, expected: int) -> None:
#     assert day_02_part_2(filename) == expected


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    print(f"Day 2 Part 1: {day_02_part_1(args.filename)}")
    # print(f"Day 2 Part 2: {day_02_part_2(args.filename)}")
