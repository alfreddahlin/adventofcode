input_data = open("inputs/day25.in", "r").read().strip().split("\n")
from_snafu = {"=": -2, "-": -1, "0": 0, "1": 1, "2": 2}
to_snafu = "=-012"

snafu = [
    sum(from_snafu[d] * 5**i for i, d in enumerate(reversed(n))) for n in input_data
]

value = sum(snafu)
snafu_sum = ""
while value != 0:
    value, rest = divmod(value + 2, 5)
    snafu_sum = to_snafu[rest] + snafu_sum

print("Part 1:", snafu_sum)
