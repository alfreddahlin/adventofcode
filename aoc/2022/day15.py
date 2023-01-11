import re

test = False
# test = True
if test:
    input_data = open("inputs/day15_test.in", "r").read().strip().split("\n")
    y = 10
    detect_range = 20
else:
    input_data = open("inputs/day15.in", "r").read().strip().split("\n")
    y = 2_000_000
    detect_range = 4_000_000


data = [list(map(int, re.findall(r"-?\d+", line))) for line in input_data]
sensors = {d[0] + d[1] * 1j: abs(d[2] - d[0]) + abs(d[3] - d[1]) for d in data}
beacons = {d[2] + d[3] * 1j for d in data}

in_range = set()
for sensor, r in sensors.items():
    extra = r - abs(y - int(sensor.imag))
    in_range.update(
        x + y * 1j
        for x in range(int(sensor.real) - extra, int(sensor.real) + extra + 1)
        if extra >= 0
    )
print(
    "Part 1:",
    len(in_range)
    - len({c for c in set(sensors.keys()) | beacons if c.imag == y and c in in_range}),
)

borders_any = set()
borders_several = set()
for s, r in sensors.items():
    borders = {
        x + s.real + (y + s.imag) * 1j
        for x in range(-r - 1, r + 2)
        for y in [abs(x) - r - 1, r - abs(x) + 1]
        if abs(x) + abs(y) == r + 1
        and 0 < x + s.real < detect_range
        and 0 < y + s.imag < detect_range
    }
    borders_several |= borders_any & borders
    borders_any |= borders

for b in borders_several:
    for s, r in sensors.items():
        if abs(s.real - b.real) + abs(s.imag - b.imag) <= r:
            break
    else:
        print("Part 2:", int(b.real * 4_000_000 + b.imag))
        break
