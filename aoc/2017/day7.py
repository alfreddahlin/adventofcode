from aoc.utils import input

data = input.get_lines(__file__, r"^([a-z]+) \((\d+)\)(?: -> (.*))?")
programs = {
    program: (int(weight), tops.split(", ") if tops else None)
    for program, weight, tops in data
}


def get_weight(program, programs):
    weight, disks = programs[program]
    if disks is None:
        return weight
    else:
        return weight + sum((get_weight(disk, programs) for disk in disks))


def get_error(program, programs, value):
    weight, disks = programs[program]
    if disks is None:
        return weight + value

    disk_weights = {}
    for disk in disks:
        disk_weight = get_weight(disk, programs)
        disk_weights[disk_weight] = disk_weights.get(disk_weight, []) + [disk]

    if len(disk_weights) == 1:
        return weight + value

    off_weight, balanced_weight = disk_weights.keys()
    if len(disk_weights[off_weight]) != 1:
        off_weight, balanced_weight = balanced_weight, off_weight

    return get_error(
        disk_weights[off_weight][0], programs, balanced_weight - off_weight
    )


tops = {top for _, tops in programs.values() if tops is not None for top in tops}
root = (set(programs.keys()) - tops).pop()
print("Part 1:", root)
print("Part 2:", get_error(root, programs, 0))
