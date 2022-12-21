from copy import deepcopy
from collections import deque

input_data = open("inputs/day20.in", "r").read().strip().split("\n")

data = [int(line) for line in input_data]
indexes = [1000, 2000, 3000]
key = 811589153
repeat = 10


def mix(data, indexes, factor=1, n=1):
    class Number:
        def __init__(self, value):
            self.value = value * factor

    l = len(data)
    new_sequence = deque(map(Number, data))
    sequence = list(new_sequence)

    for _ in range(n):
        for d in sequence:
            i = new_sequence.index(d)
            new_sequence.rotate(-i)
            new_sequence.popleft()
            new_sequence.rotate(-d.value % (l - 1))
            new_sequence.appendleft(d)

    sequence = [d.value for d in new_sequence]
    start = sequence.index(0)
    return sum(sequence[(start + i) % l] for i in indexes)


print("Part 1:", mix(data, indexes))
print("Part 2:", mix(data, indexes, key, repeat))

# Inspiration (dirty...)
# # Part 2
# numbers = [int(x) * 811589153 for x in open("inputs/day20.in")]
# indices = list(range(len(numbers)))

# for i in indices * 10:
#     indices.pop(j := indices.index(i))
#     indices.insert((j + numbers[i]) % len(indices), i)

# zero = indices.index(numbers.index(0))
# print(sum(numbers[indices[(zero + p) % len(numbers)]] for p in [1000, 2000, 3000]))
