import re

input_data = open("inputs/day16.in", "r").read().strip().split("\n")

data = [
    re.findall(
        r"^Valve ([A-Z]+) has flow rate=([-?\d]+); tunnels? leads? to valves? (.*)$",
        line,
    )
    for line in input_data
]

valves = {}
for [(valve, flow, tunnels)] in data:
    valves[valve] = (int(flow), tuple(tunnels.split(", ")))
max_flow = max(valve[0] for valve in valves.values())


def get_alternatives_prep(data, current):
    return {tunnel: 1 for tunnel in data[current][1]}


def search_prep(data, start, targets):
    cost = 0
    queue = [(start, 0)]
    seen = {start}
    result = {}
    while queue and targets:
        current, cost = queue.pop(0)
        alternatives = get_alternatives_prep(data, current)

        queue += [
            (new, cost + new_cost)
            for new, new_cost in alternatives.items()
            if new not in seen
        ]
        seen.update(alternatives.keys())
        if current in targets:
            result[current] = cost
            targets.remove(current)
    return result


def get_alternatives(data, current):
    return {key: value + 1 for key, value in data[current].items()}


# def search(data, paths, start, target_cost=None):
#     cost = 0
#     flow = 0
#     pressure = {0: 0}
#     pressure_all = set()
#     queue = [(start, 0, 0, pressure, set([start]))]
#     while queue:
#         current, cost, flow, pressure, visited = queue.pop(0)
#         curr_pressure = pressure[cost]
#         if cost >= target_cost:
#             return pressure
#         alternatives = get_alternatives(paths, current)

#         queue += [
#             (
#                 new,
#                 cost + new_cost,
#                 flow + data[new][0],
#                 pressure | {(cost + new_cost): flow * new_cost + curr_pressure},
#                 visited | {new},
#             )
#             for new, new_cost in alternatives.items()
#             if new not in visited and cost + new_cost < target_cost
#         ]
#         queue = sorted(queue, key = lambda x: x[3][1] + x[1]*flow + max((x[2]+max_flow)*(target_cost - cost), 0))
#         pressure_all.add(curr_pressure + max((target_cost - cost) * flow, 0))
#         if len(visited) == len(paths):
#             print()
#             breakpoint()

#     return max(pressure_all)


def search(data, paths, start, target_cost=None):
    cost = 0
    flow = 0
    cnt = 0
    pressure = {0: 0}
    pressure_all = set()
    queue = [(start, 0, 0, pressure, set([start]))]
    while queue:
        current, cost, flow, pressure, visited = queue.pop(0)
        curr_pressure = pressure[cost]
        if cost >= target_cost:
            return pressure
        alternatives = get_alternatives(paths, current)

        queue += [
            (
                new,
                cost + new_cost,
                flow + data[new][0],
                pressure | {(cost + new_cost): flow * new_cost + curr_pressure},
                visited | {new},
            )
            for new, new_cost in alternatives.items()
            if new not in visited and cost + new_cost < target_cost
        ]
        queue = sorted(
            queue,
            key=lambda x: x[3][x[1]]
            + x[1] * flow
            + max((x[2] + max_flow) * (target_cost - cost), 0),
        )
        pressure_all.add(curr_pressure + max((target_cost - cost) * flow, 0))
        cnt += 1
        print(cnt)
    return max(pressure_all)


pressure_valves = [valve for valve, value in valves.items() if value[0] > 0]
paths = {}
for valve in pressure_valves:
    new_paths = search_prep(
        valves,
        valve,
        {
            key
            for key in pressure_valves
            if key != valve and key not in paths.get(valve, {})
        },
    )
    paths[valve] = paths.get(valve, {})
    paths[valve].update(new_paths)
    for target, cost in new_paths.items():
        paths[target] = paths.get(target, {})
        paths[target].update({valve: cost})

paths["AA"] = search_prep(
    valves,
    "AA",
    {key for key in pressure_valves},
)
print(len(paths))
# print(search(valves, paths, "AA", 30))
