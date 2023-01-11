input_data = open("inputs/day7.in", "r").read().strip().split("\n")

data = [line.split() for line in input_data]


def add_file(directories, path, file_size):
    for folder_path in directories:
        if path.startswith(folder_path):
            directories[folder_path] += file_size


work_dir = "/"
dir_size = {work_dir: 0}
for cmd in data:
    if cmd[0] == "$":
        if cmd[1] == "cd":
            if cmd[2] == "..":
                work_dir = "/".join(work_dir.split("/")[:-2]) + "/"
            elif cmd[2] == "/":
                work_dir = "/"
            else:
                work_dir += cmd[2] + "/"
            dir_size[work_dir] = dir_size.get(work_dir, 0)
    elif cmd[0].isnumeric():
        add_file(dir_size, work_dir, int(cmd[0]))

print(
    "Part 1:",
    sum(folder_size for folder_size in dir_size.values() if folder_size <= 100000),
)

needed = dir_size["/"] + 30000000 - 70000000

print(
    "Part 2:",
    min(folder_size for folder_size in dir_size.values() if folder_size >= needed),
)


# Initial full directory build
# def get_dir(dir, path):
#     subdir = dir
#     for folder_name in path.split("/")[1:-1]:
#         folder = subdir.get(folder_name)
#         if folder is None:
#             subdir[folder_name] = {}
#         subdir = subdir[folder_name]
#     return subdir


# def get_file_size(dir):
#     if isinstance(dir, int):
#         return dir
#     else:
#         return sum([get_file_size(subdir) for subdir in dir.values()])


# def get_small_file_size(dir):
#     dir_size = sum([subdir for subdir in dir.values() if isinstance(subdir, int)])
#     subdir_size = sum(
#         [get_file_size(subdir) for subdir in dir.values() if isinstance(subdir, dict)]
#     )
#     subdir_small_size = sum(
#         [
#             get_small_file_size(subdir)
#             for subdir in dir.values()
#             if isinstance(subdir, dict)
#         ]
#     )
#     if subdir_size + dir_size <= 100000:
#         return subdir_size + dir_size + subdir_small_size
#     else:
#         return subdir_small_size


# def find_smallest(dir, needed):
#     dir_size = get_file_size(dir)
#     sub_size = [
#         find_smallest(subdir, needed)
#         for subdir in dir.values()
#         if isinstance(subdir, dict)
#     ]
#     if dir_size >= needed:
#         sub_size.append(dir_size)
#         return min(sub_size)
#     else:
#         return float("inf")


# dir = {}
# current = "/"
# cur_dir = dir
# for cmd in data:
#     if cmd[0] == "$":
#         if cmd[1] == "cd":
#             if cmd[2] == "..":
#                 current = "/".join(current.split("/")[:-2]) + "/"
#             elif cmd[2] == "/":
#                 current = cmd[2]
#             else:
#                 current += cmd[2] + "/"
#             cur_dir = get_dir(dir, current)
#     elif cmd[0] == "dir":
#         cur_dir[cmd[1]] = {}
#     elif cmd[0].isnumeric():
#         cur_dir[cmd[1]] = int(cmd[0])

# print("Part 1:", get_small_file_size(dir))
# print("Part 2:", find_smallest(dir, get_file_size(dir) + 30000000 - 70000000))
