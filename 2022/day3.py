input_data = open("inputs/day3.in", "r").read().strip().split("\n")
ord_a = ord("a") - 1
ord_A = ord("A") - 27
data = [
    ((line[: int(len(line) / 2)]), (line[int(len(line) / 2) :])) for line in input_data
]

prios = [
    [
        {ord(item) - ord_a if ord(item) > ord_a else ord(item) - ord_A for item in comp}
        for comp in pack
    ]
    for pack in data
]

print(
    "Part 1:",
    sum([a.intersection(b).pop() for a, b in prios]),
)

badges = []
prios_pack = [a.union(b) for a, b in prios]
[
    badges.append(
        prios_pack[i]
        .intersection(prios_pack[i + 1])
        .intersection(prios_pack[i + 2])
        .pop()
    )
    for i in range(0, len(prios_pack), 3)
]

print("Part 2:", sum(badges))
