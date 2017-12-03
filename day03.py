from collections import defaultdict

def task1():
    inputval = 325489
    inc = 8 # increment on each new square
    idx = 0 # number of steps to center
    sum = 1 # max number in current square
    size = 1 # square size

    # find parameters of spiral
    while(True):
        if sum < inputval:
            size += 2
            idx += 1
            sum += (idx*inc)
        else:
            break

    # find distance to start
    back_idx = sum
    while(True):
        back_idx -= (size - 1)
        if inputval >= back_idx:
            break

    center = (back_idx + sum) / 2
    distance = abs(center-inputval) + idx
    print('DIST: '+str(distance))

def sum_grid():
    grid = defaultdict(int)
    grid[0,0] = 1
    x, y = 0, 0
    f_sum = lambda x,y,grid : sum([grid[i,j] for i in range(x-1, x+2) for j in range(y-1, y+2)])
    size = 3

    while(True):
        # right for one
        x += 1; grid[x,y] = f_sum(x,y,grid); yield grid[x,y]
        # up for size - 2
        for _ in range(1,size-1): y+=1; grid[x,y] = f_sum(x,y,grid); yield grid[x,y]
        # left for size - 1
        for _ in range(1, size): x-=1; grid[x,y] = f_sum(x,y,grid); yield grid[x,y]
        # down for size - 1
        for _ in range(1, size): y-=1; grid[x,y] = f_sum(x,y,grid); yield grid[x,y]
        # right for size - 1
        for _ in range(1, size): x+=1; grid[x,y] = f_sum(x,y,grid); yield grid[x,y]
        # increase size
        size += 2

def task2():
    inputval = 325489
    for sum in sum_grid():
        if inputval < sum: print('Second solution: '+str(sum)); return

task1()
task2()