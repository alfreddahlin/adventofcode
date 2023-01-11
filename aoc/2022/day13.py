import math
import json

input_data = open("inputs/day13.in", "r").read().strip().split("\n\n")

data = [list(map(json.loads, line.split("\n"))) for line in input_data]
dividers = [[[2]], [[6]]]


def is_ordered(left, right):
    match left, right:
        case int(), int():
            return left - right
        case int(), list():
            return is_ordered([left], right)
        case list(), int():
            return is_ordered(left, [right])
        case list(), list():
            for l, r in zip(left, right):
                if diff := is_ordered(l, r):
                    return diff
            return len(left) - len(right)


sum_ordered = sum(
    [i for i, (left, right) in enumerate(data, 1) if is_ordered(left, right) < 0]
)
print("Part 1:", sum_ordered)

flat_data = [l for pair in data + [dividers] for l in pair]
divider_indexes = [
    sum(is_ordered(element, divider) <= 0 for element in flat_data)
    for divider in dividers
]
print(
    "Part 2:",
    math.prod(divider_indexes),
)

# Initial
# from functools import cmp_to_key
# ordered = sorted(
#     [l for pair in data + [dividers] for l in pair], key=cmp_to_key(is_ordered)
# )
# print("Part 2:", math.prod(ordered.index(divider) + 1 for divider in dividers))
