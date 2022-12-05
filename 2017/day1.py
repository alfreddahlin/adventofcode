import re

input_data = open("inputs/day1.in", "r").read().strip().split("\n")

data = [int(val) for val in input_data[0]]

sum_next = 0
sum_far = 0
input_length = len(data)
for i, val in enumerate(data):
    if data[(i + 1) % input_length] == val:
        sum_next += val
    if data[int((i + input_length / 2) % input_length)] == val:
        sum_far += val

print("Part 1: " + str(sum_next))
print("Part 2: " + str(sum_far))
