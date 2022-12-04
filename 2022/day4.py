import re

input_data = open("inputs/day4.in", "r").read().strip().split("\n")

data = [[int(r) for r in re.findall(r"\d+", line)] for line in input_data]

contains = [
    (f1 <= f2 and t1 >= t2) or (f1 >= f2 and t1 <= t2) for f1, t1, f2, t2 in data
]

print("Part 1:", sum(contains))

overlaps = [
    (f1 <= t2 and t1 >= f2) or (f1 >= t2 and t1 <= f2) for f1, t1, f2, t2 in data
]

print("Part 2:", sum(overlaps))

# Initial
# data = [[int(r) for r in re.findall(r"\d+", line)] for line in input_data]

# ranges = [[set(range(a, b + 1)) for a, b in pair] for pair in data]
# contains = [a <= b or b <= a for a, b in ranges]
# print("Part 1:", sum(contains))

# overlaps = [bool(a & b) for a, b in ranges]
# print("Part 2:", sum(overlaps))
