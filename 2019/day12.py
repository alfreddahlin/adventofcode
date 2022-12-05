import re

input_data = open("inputs/day12.in", "r").read().strip().split("\n")


def get_grav(c1, c2):
    return (c1 != c2) * ((c1 < c2) - (c1 > c2))


def unhash(moons, d):
    set_value = ()
    for moon in moons:
        set_value += (moons[moon]["pos"][d], moons[moon]["vel"][d])
    return set_value


moons = {}
for i, moon in enumerate(input_data):
    for pos in re.findall(r"<(.*)>", moon)[0].split(", "):
        exec(pos)

    moons[i] = {"pos": (x, y, z), "vel": (0, 0, 0)}
# moons[0]['pos'] = (-1,0,2)
# moons[1]['pos'] = (2,-10,-7)
# moons[2]['pos'] = (4,-8,8)
# moons[3]['pos'] = (3,5,-1)
moons[0]["pos"] = (-8, -10, 0)
moons[1]["pos"] = (5, 5, 10)
moons[2]["pos"] = (2, -7, 3)
moons[3]["pos"] = (9, -8, -3)

xstates = set()
ystates = set()
zstates = set()
xnew = True
ynew = True
znew = True
step = 0
while True:
    if unhash(moons, 0) not in xstates:
        xstates.add(unhash(moons, 0))
    elif xnew:
        xnew = False
        print("x:", step)

    ystates.add(unhash(moons, 1))
    zstates.add(unhash(moons, 2))
    for m1 in moons:
        for m2 in range(m1 + 1, len(moons)):
            gravity = tuple(
                get_grav(moons[m1]["pos"][i], moons[m2]["pos"][i]) for i in range(3)
            )
            moons[m1]["vel"] = tuple(v + dv for v, dv in zip(moons[m1]["vel"], gravity))
            moons[m2]["vel"] = tuple(v - dv for v, dv in zip(moons[m2]["vel"], gravity))
        moons[m1]["pos"] = tuple(
            p + v for p, v in zip(moons[m1]["pos"], moons[m1]["vel"])
        )

    step += 1

    if step == 100:
        energy = [
            (
                abs(moons[m]["pos"][0])
                + abs(moons[m]["pos"][1])
                + abs(moons[m]["pos"][2])
            )
            * (
                abs(moons[m]["vel"][0])
                + abs(moons[m]["vel"][1])
                + abs(moons[m]["vel"][2])
            )
            for m in moons
        ]
        print("Part 1:", sum(energy))

print("Part 2:", step)
