from aoc.utils import input
from aoc.utils import graph

data = input.get_grid(__file__, ord)

start_p1, end = [key for key, value in data.items() if value in {ord("S"), ord("E")}]
possible = {1, -1, 1j, -1j}
data[start_p1] = ord("a")
data[end] = ord("z")


def get_neighbors_reverse(state, _, tree):
    return [
        state + step
        for step in possible
        if state + step in tree and tree[state + step] >= tree[state] - 1
    ]


def get_cost_remaining_taxi(state, target, _):
    return abs(state - target)


def get_cost_remaining_ground(state, _, tree):
    return tree[state] - ord("a")


def is_ground_level(state, _, tree):
    return tree[state] == ord("a")


print(
    "Part 1:",
    graph.search(
        start=end,
        target=start_p1,
        tree=data,
        get_neighbors=get_neighbors_reverse,
        get_cost_remaining=get_cost_remaining_taxi,
    ),
)
print(
    "Part 2:",
    graph.search(
        start=end,
        tree=data,
        get_neighbors=get_neighbors_reverse,
        get_cost_remaining=get_cost_remaining_ground,
        is_finished=is_ground_level,
    ),
)
