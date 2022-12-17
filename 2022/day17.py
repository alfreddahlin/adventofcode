import re
from itertools import cycle

input_data = open("inputs/day17.in", "r").read().strip()

rocks = enumerate(
    cycle(
        (
            {0, 1, 2, 3},
            {1, 1j, 1 + 1j, 2 + 1j, 1 + 2j},
            {0, 1, 2, 2 + 1j, 2 + 2j},
            {0, 1j, 2j, 3j},
            {0, 1, 1j, 1 + 1j},
        )
    ),
    1,
)
pushes = {"<": -1, ">": 1}
jets = enumerate(cycle(pushes[jet] for jet in input_data))
simulate = (2022, 1e12)


def plot(cave):
    for y in range(max([int(r.imag) for r in cave]), 0, -1):
        print("|", end="")
        for x in range(1, 8):
            print("X" if x + y * 1j in cave else ".", end="")
        print("|")
    print("+-------+")


def can_move(rock, pos, jet, cave):
    new_pos = pos + jet
    width = max({r.real for r in rock}) + 1
    return (
        len({r + new_pos for r in rock} & cave) == 0
        and new_pos.real > 0
        and new_pos.real + width < 9
        and new_pos.imag > 0
    )


def cave_height(cave):
    return max([int(r.imag) for r in cave] + [0])


def principal_period(s):
    return (s + s).find(s, 1, -1)


cave = set()
n = 0
pattern = ""
first_height = 0
cycle_height = 0
while True:
    if n == simulate[0]:
        height = cave_height(cave)
    current_height = cave_height(cave)
    pos = 3 + (cave_height(cave) + 4) * 1j
    n, rock = next(rocks)
    for j, jet in jets:
        pos += can_move(rock, pos, jet, cave) * jet
        if can_move(rock, pos, -1j, cave):
            pos -= 1j
        else:
            cave.update(pos + r for r in rock)
            break
    if cycle_height == 0:
        pattern += str(cave_height(cave) - current_height)
        repetition = principal_period(pattern[100:])
        if repetition > 0:
            if first_height == 0:
                cycle_length = repetition
                first_height = cave_height(cave)
            else:
                cycle_height = cave_height(cave) - first_height
    elif n >= simulate[0] and (simulate[1] - n) % cycle_length == 0:
        remaining_cycles = int((simulate[1] - n) / cycle_length)
        break

print("Part 1:", height)
print(
    "Part 2:",
    cave_height(cave) + cycle_height * remaining_cycles,
)
