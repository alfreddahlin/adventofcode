input_data = open("inputs/day6.in", "r").read().strip()


def find_set_index(e, n):
    for i in range(n, len(e)):
        if len(set(e[i - n : i])) == n:
            return i


print("Part 1:", find_set_index(input_data, 4))
print("Part 2:", find_set_index(input_data, 14))
