import re

input_data = open('inputs/day3.in','r').read().strip().split('\n')
data = int(input_data[0])

layer = 0
while data > (2*layer+1)**2:
    layer += 1

middle_point = (2*layer+1)**2-layer
while data < middle_point-layer+1:
    middle_point -= 2*layer

walk = abs(data - middle_point)
steps = layer + walk
print('Part 1:',steps)

field = {(0,0): 1}
x,y = 0,0
dx,dy = 1,0
while data > field[(x,y)]:
    x += dx
    y += dy
    field[(x,y)] = sum(field.get((x_i,y_i),0) for x_i in range(x-1,x+2) for y_i in range(y-1,y+2))
    if dx == 1 and field.get((x,y+1),0) == 0:
        dx,dy = 0,1
    elif dy == 1 and field.get((x-1,y),0) == 0:
        dx,dy = -1,0
    elif dx == -1 and field.get((x,y-1),0) == 0:
        dx,dy = 0,-1
    elif dy == -1 and field.get((x+1,y),0) == 0:
        dx,dy = 1,0
    
print('Part 2:',field[(x,y)])


