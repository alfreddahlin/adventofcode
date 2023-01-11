from aoc.utils.input import get_input
import re
import math
from copy import deepcopy

input_data = get_input(__file__, "\n\n")


class Monkey:
    def __init__(self, monkey):
        self.items = [int(i) for i in re.findall(r"\d+", monkey[1])]
        self.factor = int(re.findall(r"\d+", monkey[3])[0])
        self.targets = [
            int(re.findall(r"\d+", monkey[5])[0]),
            int(re.findall(r"\d+", monkey[4])[0]),
        ]
        self.operation = lambda old: eval(monkey[2].split("=")[1]) % common_factor
        self.inspections = 0

    def inspect(self, group, calm=True):
        while self.items:
            item = self.operation(self.items.pop(0))
            if calm:
                item = int(item / 3)

            group[self.targets[item % self.factor == 0]].items.append(item)

            self.inspections += 1


def simulate(monkeys, n, calm=True):
    for _ in range(n):
        for monkey in monkeys:
            monkey.inspect(group=monkeys, calm=calm)
    return math.prod(sorted([monkey.inspections for monkey in monkeys])[-2:])


monkeys = list(map(Monkey, [monkey.split("\n") for monkey in input_data]))
common_factor = math.prod(monkey.factor for monkey in monkeys)

print("Part 1:", simulate(monkeys=deepcopy(monkeys), n=20, calm=True))
print("Part 2:", simulate(monkeys=deepcopy(monkeys), n=10000, calm=False))
