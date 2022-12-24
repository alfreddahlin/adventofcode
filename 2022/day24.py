input_data = open("inputs/day24.in", "r").read().strip().split("\n")

data = {
    x + y * 1j: c
    for y, line in enumerate(input_data)
    for x, c in enumerate(line)
    if c != "."
}
directions = {">": 1, "<": -1, "v": 1j, "^": -1j}
bounds = (0, len(input_data[0]) - 1, 0, len(input_data) - 1)
start = 1
goal = bounds[1] - 1 + bounds[3] * 1j


def search(bounds, storms, minute, start, target):
    queue = [(start, minute + 1)]
    seen = {(start, minute + 1)}
    while True:
        if minute == queue[0][1] - 1:
            for blizzard in storms:
                blizzard.move(bounds)

        position, minute = queue.pop(0)
        if position == target:
            return minute
        alternatives = {
            (new_position, minute + 1)
            for new_position in get_alternatives(position, bounds, storms)
            if (new_position, minute + 1) not in seen
        }
        queue.extend(alternatives)

        seen.update(alternatives)


def get_alternatives(position, bounds, storms):
    alternatives = set()
    occupied = {blizzard.position for blizzard in storms}
    for d in [0, 1, -1, 1j, -1j]:
        new_position = position + d
        if (
            (
                new_position not in occupied
                and bounds[0] < new_position.real < bounds[1]
                and bounds[2] < new_position.imag < bounds[3]
            )
            or new_position == goal
            or new_position == start
        ):
            alternatives.add(new_position)
    return alternatives


class Blizzard:
    def __init__(self, position, direction):
        self.position = position
        self.direction = directions[direction]

    def move(self, bounds):
        self.position += self.direction
        if self.position.real in bounds[:2]:
            self.position -= self.direction * (bounds[1] - 1)
            assert (self.position - self.direction).real in bounds[:2]
        elif self.position.imag in bounds[2:]:
            self.position -= self.direction * (bounds[3] - 1)
            assert (self.position - self.direction).imag in bounds[2:]
        return


storms = {Blizzard(key, value) for key, value in data.items() if value != "#"}
trip1 = search(bounds, storms, -1, start, goal)
print("Part 1:", trip1)
trip2 = search(bounds, storms, trip1, goal, start)
trip3 = search(bounds, storms, trip2, start, goal)
print("Part 2:", trip3)
