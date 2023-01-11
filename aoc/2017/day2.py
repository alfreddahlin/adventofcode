import re

input_data = open("inputs/day2.in", "r").read().strip().split("\n")

data_str = [re.findall(r"\d+", line) for line in input_data]

data = [[int(numb) for numb in line] for line in data_str]

# data = [[5, 1, 9, 5],[7, 5, 3],[2, 4, 6, 8]]
# data = [[5, 9, 2, 8],[9, 4, 7, 3],[3, 8, 6, 5]]
# map(lambda x: x.sort(), data)
for line in data:
    line.sort()

diff_sum = sum(max(line) - min(line) for line in data)

print("Part 1: " + str(diff_sum))

div_sum = 0
for line in data:
    found = False
    for l in range(len(data)):
        for h in range(len(data) - 1, l, -1):
            if line[h] % line[l] == 0:
                div_sum += int(line[h] / line[l])
                found = True
                break
        if found:
            break
print("Part 2: " + str(div_sum))
