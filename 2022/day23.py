from collections import deque
from itertools import count
from copy import deepcopy

input_data = open("inputs/day23.in", "r").read().strip().split("\n")

data = {
    x + y * 1j
    for y, line in enumerate(input_data)
    for x, elf in enumerate(line)
    if elf == "#"
}
check = {
    "N": (-1j, -1 - 1j, 1 - 1j),
    "S": (1j, -1 + 1j, 1 + 1j),
    "W": (-1, -1 - 1j, -1 + 1j),
    "E": (1, 1 - 1j, 1 + 1j),
}
order = deque(("N", "S", "W", "E"))


def plot(grove):
    x_min, x_max, y_min, y_max = get_bounds(grove)
    for y in range(y_min, y_max + 1):
        for x in range(x_min, x_max + 1):
            if x + y * 1j in grove:
                print("#", end="")
            else:
                print(".", end="")
        print()


class Elf:
    def __init__(self, position):
        self.position = position
        self.proposed = None

    def propose(self, order, grove):
        if not any(
            self.position + x + y * 1j in grove
            for x in range(-1, 2)
            for y in range(-1, 2)
            if not (x == 0 and y == 0)
        ):
            self.proposed = None
        else:
            for direction in order:
                look = [self.position + d for d in check[direction]]
                if not any(p in grove for p in look):
                    self.proposed = look[0]
                    break
            else:
                self.proposed = None
        return self.proposed

    def move(self, contested):
        if self.proposed is not None:
            self.position = (
                self.proposed if self.proposed not in contested else self.position
            )
        return


def get_bounds(grove):
    xs = [g.real for g in grove]
    ys = [g.imag for g in grove]
    return map(
        int,
        (
            min(xs),
            max(xs),
            min(ys),
            max(ys),
        ),
    )


verify = 0
elves = list(map(Elf, data))
grove = {elf.position for elf in elves}
for i in count(1):
    proposed = set()
    contested = set()
    for elf in elves:
        p = elf.propose(order, grove)
        if p is not None and p in proposed:
            contested.add(p)
        elif p is not None:
            proposed.add(p)
    if len(proposed) == 0:
        break
    for elf in elves:
        elf.move(contested)
    order.rotate(-1)
    grove = {elf.position for elf in elves}
    if i == 10:
        x_min, x_max, y_min, y_max = get_bounds(grove)
        verify = (1 + x_max - x_min) * (1 + y_max - y_min) - len(grove)
print("Part 1:", verify)
print("Part 2:", i)

# Potential improvements with batch setting
# x8 = [1, 1 + 1j, 1j, 1j - 1, -1, -1 - 1j, -1j, 1 - 1j]
# dirs = [-1j, 1j, -1, 1]


# def move(elves, p, fdir):
#     adj = elves & {p + t for t in x8}
#     if not adj:
#         return p
#     for t in range(4):
#         d = dirs[(fdir + t) % 4]
#         adj = elves & {p + d, p + d + d * 1j, p + d - d * 1j}
#         if not adj:
#             return p + d
#     return p


# def empty_ground(elves):
#     xs = [elf.real for elf in elves]
#     ys = [elf.imag for elf in elves]
#     return (max(xs) - min(xs) + 1) * (max(ys) - min(ys) + 1) - len(elves)


# def update(elves, r):
#     want = {elf: move(elves, elf, r % 4) for elf in elves}
#     c = Counter(want.values())
#     canhave = {elf for elf in want if c[want[elf]] == 1}
#     canthave = elves - canhave
#     return canthave | {want[elf] for elf in canhave}


# i = 0
# pelfs = {}
# while elfs != pelfs:
#     pelfs = elfs
#     elfs = update(elfs, i)
#     i += 1  # this round they moved
#     if i == 10:
#         print("Part 1:", empty_ground(elfs))  # part 1
# print("Part 2:", i)  # part 2
