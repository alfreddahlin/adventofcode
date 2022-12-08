import math

input_data = open("inputs/day9.in", "r").read().strip().split("\n")

data = [line.split() for line in input_data]
directions = {"R": 1, "L": -1, "D": 1j, "U": -1j}

visited_first = set()
visited_end = set()

rope = [0] * 10
for dir, steps in data:
    for _ in range(int(steps)):
        rope[0] += directions[dir]
        for knot in range(1, len(rope)):
            diff = rope[knot - 1] - rope[knot]
            if abs(diff) > math.sqrt(2):
                rope[knot] += math.copysign(diff.real != 0, diff.real)
                rope[knot] += math.copysign(diff.imag != 0, diff.imag) * 1j
        visited_first.add(rope[1])
        visited_end.add(rope[-1])

print("Part 1:", len(visited_first))
print("Part 2:", len(visited_end))

# from operator import add, sub

# directions = {"R": (1, 0), "L": (-1, 0), "D": (0, 1), "U": (0, -1)}

# visited_first = set()
# visited_end = set()

# rope = [(0, 0) for _ in range(10)]
# for dir, steps in data:
#     for _ in range(int(steps)):
#         rope[0] = list(map(add, rope[0], directions[dir]))
#         for knot in range(1, len(rope)):
#             diff = tuple(map(sub, rope[knot - 1], rope[knot]))
#             if any(abs(d) > 1 for d in diff):
#                 rope[knot] = tuple(
#                     map(
#                         add,
#                         rope[knot],
#                         map(lambda x: math.copysign(x != 0, x), diff),
#                     )
#                 )

#         visited_first.add(rope[1])
#         visited_end.add(rope[-1])

# print("Part 1:", len(visited_first))
# print("Part 2:", len(visited_end))


# visited_first = set()
# visited_end = set()

# rope = [[0, 0] for _ in range(10)]
# for dir, steps in data:
#     for _ in range(int(steps)):
#         rope[0] = list(map(add, rope[0], directions[dir]))
#         for knot in range(1, len(rope)):
#             side_diff, vertical_diff = map(sub, rope[knot - 1], rope[knot])
#             if abs(side_diff) > 1 or abs(vertical_diff) > 1:
#                 rope[knot][0] += math.copysign(side_diff != 0, side_diff)
#                 rope[knot][1] += math.copysign(vertical_diff != 0, vertical_diff)

#         visited_first.add(tuple(rope[1]))
#         visited_end.add(tuple(rope[-1]))

# print("Part 1:", len(visited_first))
# print("Part 2:", len(visited_end))
