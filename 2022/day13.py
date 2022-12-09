from functools import cmp_to_key

input_data = open("inputs/day13.in", "r").read().strip().split("\n\n")


def is_ordered(left, right):
    if isinstance(left, list) and isinstance(right, list):
        if len(right) == 0 and len(left) == 0:
            return 0
        elif len(right) == 0 or len(left) == 0:
            if len(left) == 0:
                return -1
            else:
                return 1
    elif isinstance(left, list):
        if len(left) == 0:
            return -1
        right = [right]
    elif isinstance(right, list):
        if len(right) == 0:
            return 1
        left = [left]
    else:
        if left == right:
            return 0
        else:
            if left < right:
                return -1
            else:
                return 1
    for i in range(min(len(left), len(right))):
        ordered = is_ordered(left[i], right[i])
        if ordered != 0:
            return ordered
    if len(left) == len(right):
        return 0
    elif len(left) < len(right):
        return -1
    else:
        return 1


data = [list(map(eval, line.split("\n"))) for line in input_data]

sum_ordered = 0
for i, (left, right) in enumerate(data):
    ordered = None
    while ordered is None:
        ordered = is_ordered(left, right)
    sum_ordered += (ordered < 0) * (i + 1)
print("Part 1:", sum_ordered)

dividers = [[[2]], [[6]]]
data.append(dividers)
data = sorted([l for pair in data for l in pair], key=cmp_to_key(is_ordered))
print("Part 2:", (data.index(dividers[0]) + 1) * (data.index(dividers[1]) + 1))
