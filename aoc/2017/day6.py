from aoc.utils import input
from itertools import count

data = input.get_numbers(__file__)

n = len(data)
seen = set()
first = None
cycle = 0
for cycle in count(1):
    seen.add(tuple(data))
    max_memory = max(data)
    max_index = data.index(max_memory)
    data[max_index] = 0
    divisor, rest = divmod(max_memory, n)
    data = [
        memory + divisor + (1 if (i - max_index - 1) % n < rest else 0)
        for i, memory in enumerate(data)
    ]
    state = tuple(data)

    if first is None and state in seen:
        first = state
        first_cycle = cycle
    elif first is None:
        seen.add(state)
    elif state == first:
        cycle_length = cycle - first_cycle
        break


print("Part 1:", first_cycle)
print("Part 2:", cycle_length)
