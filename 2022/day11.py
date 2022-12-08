import re
import math
from copy import deepcopy

input_data = open("inputs/day11.in", "r").read().strip().split("\n\n")


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
        for item in monkey.items:
            item = monkey.operation(item)
            if calm:
                item = int(item / 3)

            group[monkey.targets[item % monkey.factor == 0]].items.append(item)

            monkey.inspections += 1
        monkey.items = []


monkeys = list(map(Monkey, [monkey.split("\n") for monkey in input_data]))
common_factor = math.prod(monkey.factor for monkey in monkeys)


monkeys_calm = deepcopy(monkeys)
for tick in range(20):
    for monkey in monkeys_calm:
        monkey.inspect(group=monkeys_calm)

inspections_calm = sorted([monkey.inspections for monkey in monkeys_calm])[-2:]
print("Part 1:", math.prod(inspections_calm))

for tick in range(10000):
    for monkey in monkeys:
        monkey.inspect(group=monkeys, calm=False)
inspections = sorted([monkey.inspections for monkey in monkeys])[-2:]
print("Part 2:", math.prod(inspections))
