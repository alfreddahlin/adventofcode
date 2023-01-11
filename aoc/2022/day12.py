import re

input_data = open("inputs/day12.in", "r").read().strip().split("\n")

data = {
    x + y * 1j: ord(c) for y, line in enumerate(input_data) for x, c in enumerate(line)
}
start_p1, end = [key for key, value in data.items() if value in {ord("S"), ord("E")}]
possible = {1, -1, 1j, -1j}
data[start_p1] = ord("a")
data[end] = ord("z")


def find_steps(data, start, target=None):
    steps = 0
    queue = [(start, 0)]
    seen = {start}
    while queue:
        current, steps = queue.pop(0)
        if current == target or (target is None and data[current] == ord("a")):
            return steps
        alternatives = [
            current + step
            for step in possible
            if current + step in data and data[current + step] >= data[current] - 1
        ]
        queue += [(new, steps + 1) for new in alternatives if new not in seen]
        seen.update(alternatives)
    return None


print("Part 1:", find_steps(data, end, start_p1))
print("Part 2:", find_steps(data, end))


# Initials

# # A* heuristic
# current = start_p1
# steps = 0
# alternatives = {}
# visited = {current}
# while current != end:
#     for step in possible:
#         if (
#             current + step not in visited
#             and current + step in data
#             and data[current + step] - data[current] <= 1
#         ):
#             alternatives[current + step] = min(
#                 steps + 1, alternatives.get(current + step, steps + 1)
#             )
#     current = sorted(
#         alternatives.keys(),
#         key=lambda x: alternatives[x] + abs(end - current),  # A* (BFS also works)
#     )[0]
#     steps = alternatives.pop(current)
#     visited.add(current)

# print("Part 1:", steps)

# # Breadth first search
# current = end
# steps = 0
# alternatives = {}
# visited = {current}
# while data[current] != ord("a"):
#     for step in possible:
#         if (
#             current + step not in visited
#             and current + step in data
#             and data[current + step] - data[current] >= -1  # Searching backwards
#         ):
#             alternatives[current + step] = min(
#                 steps + 1, alternatives.get(current + step, steps + 1)
#             )
#     current = sorted(
#         alternatives.keys(),
#         key=lambda x: alternatives[x],  # BFS
#     )[0]
#     steps = alternatives.pop(current)
#     visited.add(current)

# print("Part 2:", steps)

# Initial A* for all paths
# trails = {}
# for start in [start for start, height in data.items() if height == ord("a")]:
#     current = start
#     steps = 0
#     alternatives = {}
#     visited = {current}
#     while current != end:
#         for step in possible:
#             if (
#                 current + step not in visited
#                 and current + step in data
#                 and data[current + step] - data[current] <= 1
#             ):
#                 alternatives[current + step] = min(
#                     steps + 1, alternatives.get(current + step, steps + 1)
#                 )
#         if len(alternatives) == 0:
#             break
#         current = sorted(
#             alternatives.keys(),
#             key=lambda x: alternatives[x] + abs(end - current),
#         )[0]
#         steps = alternatives.pop(current)
#         visited.add(current)
#     else:
#         trails[start] = steps

# print("Part 1:", trails[start_p1])
# print("Part 2:", min(trails.values()))
