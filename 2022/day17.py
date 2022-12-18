from itertools import cycle

input_data = open("inputs/day17_test.in", "r").read().strip()

pushes = {"<": -1, ">": 1}
jets = enumerate(cycle(pushes[jet] for jet in input_data))
rocks = (
    {0, 1, 2, 3},
    {1, 1j, 1 + 1j, 2 + 1j, 1 + 2j},
    {0, 1, 2, 2 + 1j, 2 + 2j},
    {0, 1j, 2j, 3j},
    {0, 1, 1j, 1 + 1j},
)
rocks_cycle = enumerate(cycle(rocks), 1)
simulate = (2022, 1e12)


def plot(cave):
    for y in range(max([int(r.imag) for r in cave]), 0, -1):
        print("|", end="")
        for x in range(1, 8):
            print("X" if x + y * 1j in cave else ".", end="")
        print("|")
    print("+-------+")


def can_move(rock, pos, delta, cave):
    new_pos = pos + delta
    width = max({r.real for r in rock}) + 1
    return (
        len({r + new_pos for r in rock} & cave) == 0
        and new_pos.real > 0
        and new_pos.real + width < 9
        and new_pos.imag > 0
    )


def cave_height(cave):
    return int(max([r.imag for r in cave] + [0]))


cave = set()
n = 0
seen = {}
cycle_length = 0
while True:
    if n == simulate[0]:
        height = cave_height(cave)
    current_height = cave_height(cave)
    pos = 3 + (cave_height(cave) + 4) * 1j
    n, rock = next(rocks_cycle)
    for j, jet in jets:
        pos += can_move(rock, pos, jet, cave) * jet
        if can_move(rock, pos, -1j, cave):
            pos -= 1j
        else:
            cave.update(pos + r for r in rock)
            break
    if cycle_length == 0 and n > 10:
        key = (j % len(input_data), n % len(rocks))
        if key in seen:
            cycle_length = n - seen[key][0]
            cycle_height = cave_height(cave) - seen[key][1]
        else:
            seen[key] = (n, cave_height(cave))
    elif n >= simulate[0] and (simulate[1] - n) % cycle_length == 0:
        remaining_cycles = int((simulate[1] - n) / cycle_length)
        break

print("Part 1:", height)
print(
    "Part 2:",
    cave_height(cave) + cycle_height * remaining_cycles,
)
