input_data = open("inputs/day1.in", "r").read().strip().split("\n\n")

data = ((int(calory) for calory in input.split("\n")) for input in input_data)

sum_calories = [sum(calories) for calories in data]

print("Part 1:", max(sum_calories))

print("Part 2:", sum(sorted(sum_calories, reverse=True)[0:3]))
