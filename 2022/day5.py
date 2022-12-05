import re
from copy import deepcopy

input_data = open("inputs/day5.in", "r").read()

stacks_data, instructions_data = (
    t.split("\n") for t in input_data.strip("\n").split("\n\n")
)

instructions = [map(int, re.findall(r"\d+", line)) for line in instructions_data]

stacks_9000 = {
    int(i): list("".join(stack).strip())[::-1]
    for *stack, i in zip(*stacks_data)
    if i.isdigit()
}
stacks_9001 = deepcopy(stacks_9000)

for moves, src, dst in instructions:
    for move in range(moves):
        stacks_9000[dst].append(stacks_9000[src].pop(-1))
    stacks_9001[dst] += stacks_9001[src][-moves:]
    stacks_9001[src] = stacks_9001[src][:-moves]

print("Part 1:", "".join(stack[-1] for stack in stacks_9000.values()))
print("Part 2:", "".join(stack[-1] for stack in stacks_9001.values()))
