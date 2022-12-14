import re

input_data = open("inputs/day14.in", "r").read().strip().split("\n")

data = [[map(int, c.split(",")) for c in line.split(" -> ")] for line in input_data]
source = 500
fall = [1j, -1 + 1j, 1 + 1j]

cave = set()
for path in data:
    x_s, y_s = path[0]
    for x, y in path[1:]:
        cave |= {
            x_i + y_i * 1j
            for x_i in range(min(x, x_s), max(x, x_s) + 1)
            for y_i in range(min(y, y_s), max(y, y_s) + 1)
        }
        x_s, y_s = x, y

abyss = int(max([p.imag for p in cave]))

p = source
sands = 0
p1 = None
while source not in cave:
    for f in fall:
        if p + f not in cave and p.imag < abyss + 1:
            p += f
            break
    else:
        if p.imag >= abyss and p1 is None:
            p1 = sands
        sands += 1
        cave.add(p)
        p = source

print("Part 1:", p1)
print("Part 2:", sands)
