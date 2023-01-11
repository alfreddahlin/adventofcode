import re
from copy import deepcopy

input_data = open("inputs/day22.in", "r").read().split("\n\n")

field = {
    x + y * 1j: c
    for y, line in enumerate(input_data[0].split("\n"), 1)
    for x, c in enumerate(line, 1)
    if c not in " \n"
}
moves = [
    (int(move), turn)
    for move, turn in re.findall(r"([\d]+)([RL]?)", input_data[1].strip())
]

start = min(field, key=lambda x: (x.imag, x.real))
turns = {"L": -1j, "R": 1j, "": 1}
direction = {1: 0, 1j: 1, -1: 2, -1j: 3}
direction_3 = {1: 0, 1j: 1, -1: 2, -1j: 3}
facing_plot = {1: ">", 1j: "v", -1: "<", -1j: "^"}
size = 50


def plot(field):
    for y in range(1, int(max([f.imag for f in field])) + 1):
        for x in range(1, int(max([f.real for f in field])) + 1):
            print(field.get(x + 1j * y, " "), end="")
        print()


def wrap(field, position, facing):
    wrap = position
    while wrap - facing in field:
        wrap -= facing
    return wrap


def wrap_cube(position, facing, it):
    if position.real == 50 and 1 <= position.imag <= 50 and facing == -1:  # edge 1
        wrap = 1 + (151 - position.imag) * 1j  # to 4
        new_facing = -facing
    elif position.real == 0 and 101 <= position.imag <= 150 and facing == -1:  # edge 4
        wrap = 51 + (151 - position.imag) * 1j  # to 1
        new_facing = -facing

    elif position.real == 50 and 51 <= position.imag <= 100 and facing == -1:  # edge 2
        wrap = position.imag - 50 + 101j  # to 3
        new_facing = facing * -1j
    elif 1 <= position.real <= 50 and position.imag == 100 and facing == -1j:  # edge 3
        wrap = 51 + (position.real + 50) * 1j  # to 2
        new_facing = facing * 1j

    elif position.real == 0 and 151 <= position.imag <= 200 and facing == -1:  # edge 5
        wrap = position.imag - 100 + 1j  # to 14
        new_facing = facing * -1j
    elif 51 <= position.real <= 100 and position.imag == 0 and facing == -1j:  # edge 14
        wrap = 1 + (position.real + 100) * 1j  # to 5
        new_facing = facing * 1j

    elif 1 <= position.real <= 50 and position.imag == 201 and facing == 1j:  # edge 6
        wrap = position.real + 100 + 1j  # to 13
        new_facing = facing
    elif (
        101 <= position.real <= 150 and position.imag == 0 and facing == -1j
    ):  # edge 13
        wrap = position.real - 100 + 200j  # to 6
        new_facing = facing

    elif position.real == 51 and 151 <= position.imag <= 200 and facing == 1:  # edge 7
        wrap = position.imag - 100 + 150j  # to 8
        new_facing = facing * -1j
    elif 51 <= position.real <= 100 and position.imag == 151 and facing == 1j:  # edge 8
        wrap = 50 + (position.real + 100) * 1j  # to 7
        new_facing = facing * 1j

    elif position.real == 101 and 101 <= position.imag <= 150 and facing == 1:  # edge 9
        wrap = 150 + (151 - position.imag) * 1j  # to 12
        new_facing = -facing
    elif position.real == 151 and 1 <= position.imag <= 50 and facing == 1:  # edge 12
        wrap = 100 + (151 - position.imag) * 1j  # to 9
        new_facing = -facing

    elif position.real == 101 and 51 <= position.imag <= 100 and facing == 1:  # edge 10
        wrap = position.imag + 50 + 50j  # to 11
        new_facing = facing * -1j
    elif (
        101 <= position.real <= 151 and position.imag == 51 and facing == 1j
    ):  # edge 11
        wrap = 100 + (position.real - 50) * 1j  # to 10
        new_facing = facing * 1j
    else:
        print("not found", position, facing)
        exit()

    return (wrap, new_facing)


def move(field, moves, cube=False):
    facing = 1
    position = start
    it = 0
    for steps, turn in moves:
        it += 1
        for _ in range(steps):
            field[position] = facing_plot[facing]
            new_position = position + facing
            new_facing = facing
            match field.get(new_position):
                case "#":
                    break
                case None:
                    if cube:
                        new_position, new_facing = wrap_cube(new_position, facing, it)
                    else:
                        new_position = wrap(field, new_position, facing)
                    if field[new_position] == "#":
                        new_position = position
                        new_facing = facing
                        break
            position = new_position
            facing = new_facing
            field[position] = facing_plot[facing]
        facing *= turns[turn]
    return int(1000 * position.imag + 4 * position.real + direction[facing])


print("Part 1:", move(deepcopy(field), moves))
print("Part 2:", move(deepcopy(field), moves, True))

# Inspiration, pretty similar but cleaner
# import re

# *grid, _, path = open('inputs/day22.in')
# pos, dir = grid[0].index('.') * 1j, 1j
# grid = {(x+y*1j): c for x,l in enumerate(grid)
#                     for y,c in enumerate(l) if c in '.#'}

# def wrap(pos,dir):
#     x, y = pos.real, pos.imag
#     match dir, x//50, y//50:
#         case  1j, 0, _: return complex(149-x, 99), -1j
#         case  1j, 1, _: return complex( 49,x+ 50), -1
#         case  1j, 2, _: return complex(149-x,149), -1j
#         case  1j, 3, _: return complex(149,x-100), -1
#         case -1j, 0, _: return complex(149-x,  0),  1j
#         case -1j, 1, _: return complex(100,x- 50),  1
#         case -1j, 2, _: return complex(149-x, 50),  1j
#         case -1j, 3, _: return complex(  0,x-100),  1
#         case  1 , _, 0: return complex(  0,y+100),  1
#         case  1 , _, 1: return complex(100+y, 49), -1j
#         case  1 , _, 2: return complex(-50+y, 99), -1j
#         case -1 , _, 0: return complex( 50+y, 50),  1j
#         case -1 , _, 1: return complex(100+y,  0),  1j
#         case -1 , _, 2: return complex(199,y-100), -1

# for move in re.findall(r'\d+|[RL]', path):
#     match move:
#         case 'L': dir *= +1j
#         case 'R': dir *= -1j
#         case _:
#             for _ in range(int(move)):
#                 p, d = pos + dir, dir
#                 if p not in grid: p, d = wrap(p, d)
#                 if grid[p] == '.': pos, dir = p, d

# print(1000 * (pos.real+1) + 4 * (pos.imag+1) + [1j,1,-1j,-1].index(dir))
