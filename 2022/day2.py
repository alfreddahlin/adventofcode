import re

input_data = open("inputs/day2.in", "r").read().strip().split("\n")

point_key = {"A": 1, "B": 2, "C": 3}
win_key = {"A": ("C", "A", "B"), "B": ("A", "B", "C"), "C": ("B", "C", "A")}
result_key = {"X": 0, "Y": 1, "Z": 2}
me = {"X": "A", "Y": "B", "Z": "C"}



data = [rps.split(" ") for rps in input_data]

points1 = sum(
    [
        point_key[me[i]] + 3 * (e == me[i]) + 6 * (e == win_key[me[i]][0])
        for (e, i) in data
    ]
)

print("Part 1:", points1)

points2 = sum(
    [
        point_key[win_key[e][result_key[i]]] + 3 * (i == "Y") + 6 * (i == "Z")
        for (e, i) in data
    ]
)

print("Part 2:", points2)