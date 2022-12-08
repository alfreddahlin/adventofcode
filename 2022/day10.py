import re

input_data = open("inputs/day10.in", "r").read().strip().split("\n")

data = input_data
ss_index = [40 * i + 20 for i in range(6)]
reg_x = 1
cycles = [1]

for op in data:
    cycles.append(reg_x)
    if op.startswith("addx"):
        reg_x += int(op.split()[1])
        cycles.append(reg_x)

print("Part 1:", sum(cycles[i - 1] * i for i in ss_index))

pix = ""
for c, i in enumerate(cycles[:-1]):
    sprite = c % 40
    if sprite == 0:
        pix += "\n"
    if sprite in range(i - 1, i + 2):
        pix += "█"
    else:
        pix += " "

print("Part 2:", pix)
