from collections import defaultdict
import operator

grid = defaultdict(int)

def change_dir(prev_dir, new_dir):
    if prev_dir == (0,0) and new_dir == 'L':
        return (0,-1)
    elif prev_dir == (0,0) and new_dir == 'R':
        return (0,1)
    elif prev_dir == (0,-1) and new_dir == 'L':
        return (1,0)
    elif prev_dir == (0, -1) and new_dir == 'R':
        return (-1,0)
    elif prev_dir == (1,0) and new_dir == 'L':
        return (0,1)
    elif prev_dir == (1,0) and new_dir == 'R':
        return (0,-1)
    elif prev_dir == (-1,0) and new_dir == 'L':
        return (0,-1)
    elif prev_dir == (-1,0) and new_dir == 'R':
        return (0,1)
    elif prev_dir == (0,1) and new_dir == 'R':
        return (1,0)
    elif prev_dir == (0,1) and new_dir == 'L':
        return (-1,0)
    return None

with open('day22_input.txt', 'r') as file:
    for (idx,row) in enumerate(file.readlines()):
        row = row.replace('.','0').replace('#','2').strip('\n')
        for j in range(len(row)):
            grid[idx,j] = int(row[j])

steps = 0
direction = (0,0)
pos = (12,12)
infect_count = 0
while(steps < 10000000):
    steps += 1
    if grid[pos] == 0:
        direction = change_dir(direction, 'L')
        grid[pos] += 1
    elif grid[pos] == 1:
        grid[pos] += 1
        infect_count += 1
    elif grid[pos] == 2:
        grid[pos] = -1
        direction = change_dir(direction, 'R')
    elif grid[pos] == -1:
        grid[pos] += 1
        direction = tuple(map(operator.mul, direction, (-1,-1)))

    pos = tuple(map(operator.add, pos, direction))

print(infect_count)