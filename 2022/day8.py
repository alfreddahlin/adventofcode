input_data = open("inputs/day8.in", "r").read().strip().split("\n")

data = input_data
data_t = ["".join(row) for row in zip(*data)]
visible = 0
max_view_product = 0
for y, row in enumerate(data):
    for x, tree in enumerate(row):
        col = data_t[x]
        if x in [0, len(row) - 1] or y in [0, len(col) - 1]:
            visible += 1
        else:
            left = row[:x][::-1]
            right = row[x + 1 :]
            up = col[:y][::-1]
            down = col[y + 1 :]
            if (
                max(left) < tree
                or max(right) < tree
                or max(up) < tree
                or max(down) < tree
            ):
                visible += 1
            view_left = next(
                (i + 1 for i, height in enumerate(left) if height >= tree), x
            )
            view_right = next(
                (i + 1 for i, height in enumerate(right) if height >= tree),
                len(right),
            )
            view_up = next((i + 1 for i, height in enumerate(up) if height >= tree), y)
            view_down = next(
                (i + 1 for i, height in enumerate(down) if height >= tree),
                len(down),
            )
            view_product = (
                int(view_left) * int(view_right) * int(view_up) * int(view_down)
            )
            max_view_product = max(view_product, max_view_product)


print("Part 1:", visible)
print("Part 2:", max_view_product)
