from aoc.utils import input
from aoc.utils import graph

data = input.get_lines(
    __file__,
    r"^Valve ([A-Z]+) has flow rate=([-?\d]+); tunnels? leads? to valves? (.*)$",
)
target_time = 30
start_valve = "AA"
# State index definition
time_index, pressure_index, flow_index, valve_index = range(4)

valves = {}
for valve, flow, tunnels in data:
    valves[valve] = (int(flow), tuple(tunnels.split(", ")))
max_flow = max(valve[0] for valve in valves.values())


def get_neighbors_full(state, target, tree):
    return {tunnel: 1 for tunnel in tree[state][1]}


# Create path map containing costs between all valves with pressure
pressure_valves = [valve for valve, value in valves.items() if value[0] > 0]
paths = {}
for valve in pressure_valves:
    new_paths = {
        target: graph.search(
            start=valve,
            target=target,
            tree=valves,
            get_neighbors=get_neighbors_full,
        )
        for target in pressure_valves
        if target != valve and target not in paths.get(valve, {})
    }
    paths[valve] = paths.get(valve, {"pressure": -valves[valve][0], "tunnels": {}})
    paths[valve]["tunnels"].update(new_paths)

    # Adds reversed path to reduce searches
    for target, cost in new_paths.items():
        paths[target] = paths.get(
            target, {"pressure": -valves[target][0], "tunnels": {}}
        )
        paths[target]["tunnels"].update({valve: cost})

# Only add paths from AA as starting point
paths[start_valve] = {
    "pressure": valves[start_valve][0],
    "tunnels": {
        target: graph.search(
            start=start_valve,
            target=target,
            tree=valves,
            get_neighbors=get_neighbors_full,
        )
        for target in pressure_valves
    },
}


def get_neighbors(state, target, tree):
    # Adding +1 to cost for time to open valve
    neighbors = {
        (
            state[time_index] + (cost + 1),
            state[pressure_index] + (cost + 1) * state[flow_index],
            state[flow_index] + tree[valve]["pressure"],
            valve,
            *state[valve_index:],
        )
        for valve, cost in tree[state[valve_index]]["tunnels"].items()
        if valve not in state and state[time_index] + (cost + 1) < target
    }

    # Check if last valve gets opened, in that case extrapolate to end time
    if len(neighbors) <= 1:
        if neighbors:
            base_state = neighbors.pop()
        else:
            base_state = state
        neighbors = {
            (
                target,
                base_state[pressure_index]
                + (target - base_state[time_index]) * base_state[flow_index],
                base_state[flow_index],
                *base_state[valve_index:],
            )
        }
    return neighbors


# Pressure of next state used as cost
def get_pressure(state, neighbor, _):
    return neighbor[pressure_index] - state[pressure_index]


# Time of next state used as priority
def get_time(state, neighbor, _):
    return state[time_index] - state[pressure_index]


def is_finished(state, target, tree):
    return state[time_index] == target


# State represented as tuple of time, pressure, flow, current valve, [opened valves]
print(
    "Part 1:",
    -graph.search(
        start=(0, 0, 0, start_valve),
        target=target_time,
        tree=paths,
        get_neighbors=get_neighbors,
        get_cost=get_pressure,
        get_cost_remaining=get_time,
        is_finished=is_finished,
    ),
)
