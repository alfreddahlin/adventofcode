from aoc.utils import input

data = input.get_numbers(__file__)

operations = data.copy()
steps = 0
i = 0
while 0 <= i < len(operations):
    next = i + operations[i]
    operations[i] += 1
    i = next
    steps += 1
print("Part 1:", steps)

operations_conditional = data.copy()
steps_conditional = 0
i = 0
while 0 <= i < len(operations_conditional):
    next = i + operations_conditional[i]
    operations_conditional[i] += 1 if operations_conditional[i] < 3 else -1
    i = next
    steps_conditional += 1
print("Part 2:", steps_conditional)
