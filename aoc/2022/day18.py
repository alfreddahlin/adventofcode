input_data = open("inputs/day18.in", "r").read().strip().split("\n")
adjacent = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))

data = {tuple(int(c) for c in line.split(",")) for line in input_data}
min_dim = min(min(c) for c in zip(*data))
max_dim = max(max(c) for c in zip(*data))


def find_surfaces(data, start):
    surfaces = 0
    queue = [start]
    seen = {start}
    while queue:
        current = queue.pop(0)
        alternatives = get_neighbors(current)
        surfaces += sum(1 for n in alternatives if n in data)
        queue += {
            new
            for new in alternatives
            if new not in seen
            and new not in data
            and all(min_dim - 1 <= n <= max_dim + 1 for n in new)
        }
        seen.update(alternatives)
    return surfaces


def get_neighbors(current):
    return {tuple(current[i] + a[i] for i in range(3)) for a in adjacent}


surfaces = 0
for c in data:
    surfaces += 6 - sum(n in data for n in get_neighbors(c))

print("Part 1:", surfaces)
print("Part 2:", find_surfaces(data, (0, 0, 0)))
