import argparse
import collections
import os.path
import functools
import pytest

INPUT_TXT = os.path.join(os.path.dirname(__file__), 'input.txt')
EXAMPLE_TXT = os.path.join(os.path.dirname(__file__), 'example.txt')


def day_11_part_1(filename: str) -> int:
    with open(filename) as f:
        input = [l.strip() for l in f]

    class Monkey:
        def __init__(self, items: list[int], operation: str, operation_amount: str, test: int, test_true: int, test_false: int) -> None:
            self.items = collections.deque(items)
            self.items_inspected = 0
            self.operation = operation  # '+' or '*'
            self.operation_amount = operation_amount  # int or 'old'
            self.test = test  # amount to test if worry level is divisible by
            self.test_true = test_true  # monkey to throw to if test is true
            self.test_false = test_false  # monkey to throw to if test is false

        def __str__(self) -> str:
            return f"Inspected: {self.items_inspected}, Items: {self.items}"

        def inspect(self) -> None:
            if len(self.items) == 0:
                return

            self.items_inspected += 1
            amount = self.items[0] if self.operation_amount == "old" else int(
                self.operation_amount)
            match self.operation:
                case '+': self.items[0] += amount
                case '*': self.items[0] *= amount
                case _: raise Exception("Invalid operation")
            self.items[0] = self.items[0] // 3

        def throw_to(self) -> int:
            if self.items[0] % self.test == 0:
                return self.test_true
            return self.test_false

    # Build Monkeys
    monkeys: list[Monkey] = []
    for i in range(0, len(input), 7):
        # Parse items
        string_items = input[i + 1].split(' ')
        items = []
        for s in string_items[2:]:
            if s[-1] == ',':
                items.append(int(s[:-1]))
            else:
                items.append(int(s))

        # Parse operation
        string_operation = input[i + 2].split(' ')
        operation = string_operation[4]
        operation_amount = string_operation[5] if string_operation[5] == "old" else int(
            string_operation[5])

        # Parse test
        test = int(input[i + 3].split(' ')[-1])
        test_true = int(input[i + 4].split(' ')[-1])
        test_false = int(input[i + 5].split(' ')[-1])

        monkeys.append(Monkey(items, operation, operation_amount,
                       test, test_true, test_false))

    # Play Keep Away
    for _ in range(20):
        for m in range(len(monkeys)):
            for i in range(len(monkeys[m].items)):
                monkeys[m].inspect()
                target_monkey = monkeys[m].throw_to()
                monkeys[target_monkey].items.append(monkeys[m].items.popleft())

    # Calculate Monkey Business
    monkey_business = [0, 0]
    for m in monkeys:
        if m.items_inspected > monkey_business[0]:
            monkey_business[1] = monkey_business[0]
            monkey_business[0] = m.items_inspected
        elif m.items_inspected > monkey_business[1]:
            monkey_business[1] = m.items_inspected

    return monkey_business[0] * monkey_business[1]


def day_11_part_2(filename: str) -> int:
    with open(filename) as f:
        input = [l.strip() for l in f]

    class Monkey:
        def __init__(self, items: list[int], operation: str, operation_amount: str, test: int, test_true: int, test_false: int) -> None:
            self.items = collections.deque(items)
            self.items_inspected = 0
            self.operation = operation  # '+' or '*'
            self.operation_amount = operation_amount  # int or 'old'
            self.test = test  # amount to test if worry level is divisible by
            self.test_true = test_true  # monkey to throw to if test is true
            self.test_false = test_false  # monkey to throw to if test is false

        def __str__(self) -> str:
            return f"Inspected: {self.items_inspected}, Items: {self.items}"

        def inspect(self, modulo: int) -> None:
            if len(self.items) == 0:
                return

            self.items_inspected += 1
            amount = self.items[0] if self.operation_amount == "old" else int(
                self.operation_amount)
            match self.operation:
                case '+': self.items[0] += amount
                case '*': self.items[0] *= amount
                case _: raise Exception("Invalid operation")
            self.items[0] %= modulo

        def throw_to(self) -> int:
            if self.items[0] % self.test == 0:
                return self.test_true
            return self.test_false

    # Build Monkeys
    monkeys: list[Monkey] = []
    for i in range(0, len(input), 7):
        # Parse items
        string_items = input[i + 1].split(' ')
        items = []
        for s in string_items[2:]:
            if s[-1] == ',':
                items.append(int(s[:-1]))
            else:
                items.append(int(s))

        # Parse operation
        string_operation = input[i + 2].split(' ')
        operation = string_operation[4]
        operation_amount = string_operation[5] if string_operation[5] == "old" else int(
            string_operation[5])

        # Parse test
        test = int(input[i + 3].split(' ')[-1])
        test_true = int(input[i + 4].split(' ')[-1])
        test_false = int(input[i + 5].split(' ')[-1])

        monkeys.append(Monkey(items, operation, operation_amount,
                       test, test_true, test_false))

    # Calculate Global Monkey Modulo
    GLOBAL_MONKEY_MODULO = 1
    for m in monkeys:
        GLOBAL_MONKEY_MODULO *= m.test

    # Play Keep Away
    for _ in range(10_000):
        for m in range(len(monkeys)):
            for i in range(len(monkeys[m].items)):
                monkeys[m].inspect(GLOBAL_MONKEY_MODULO)
                target_monkey = monkeys[m].throw_to()
                monkeys[target_monkey].items.append(monkeys[m].items.popleft())

    # Calculate Monkey Business
    monkey_business = [0, 0]
    for m in monkeys:
        if m.items_inspected > monkey_business[0]:
            monkey_business[1] = monkey_business[0]
            monkey_business[0] = m.items_inspected
        elif m.items_inspected > monkey_business[1]:
            monkey_business[1] = m.items_inspected

    return monkey_business[0] * monkey_business[1]


@pytest.mark.parametrize(
    ("filename", "expected"),
    (
        (EXAMPLE_TXT, 10605),
        (INPUT_TXT, 99852),
    )
)
def test_day_11_part_1(filename: str, expected: int) -> None:
    assert day_11_part_1(filename) == expected


@pytest.mark.parametrize(
    ("filename", "expected"),
    (
        (EXAMPLE_TXT, 2713310158),
        (INPUT_TXT, 25935263541),
    )
)
def test_day_11_part_2(filename: str, expected: int) -> None:
    assert day_11_part_2(filename) == expected


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', nargs='?', default=INPUT_TXT)
    args = parser.parse_args()

    print(f"Day 11 Part 1: {day_11_part_1(args.filename)}")
    print(f"Day 11 Part 2: {day_11_part_2(args.filename)}")
