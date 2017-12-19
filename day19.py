from collections import defaultdict

walk = []

def walk_grid(grid, dir, x, y):
    global walk
    cnt = 0
    while(True):
        if cnt > 100000 or len(walk) == 9:
            print(cnt)
            print(walk)
            break
        cnt +=1
        if dir == 'D':
            if grid[x][y] == '|':
                x += 1; continue
            elif grid[x][y] == '-':
                x += 1; continue
            elif grid[x][y] == '+':
                if y > 0 and grid[x][y-1] == '-':
                    y -= 1; dir = 'L'; continue
                elif y < len(grid[x])-1 and grid[x][y+1] == '-':
                    y += 1; dir = 'R'; continue
            else:
                walk.append(grid[x][y])
                x += 1; continue
        
        elif dir == 'U':
            if grid[x][y] == '|':
                x -= 1; continue
            elif grid[x][y] == '-':
                x -= 1; continue
            elif grid[x][y] == '+':
                if y > 0 and grid[x][y-1] == '-':
                    y -= 1; dir = 'L'; continue
                elif y < len(grid[x])-1 and grid[x][y+1] == '-':
                    y += 1; dir = 'R'; continue
            else:
                walk.append(grid[x][y])
                x -= 1; continue
        
        elif dir == 'R':
            if grid[x][y] == '|':
                y += 1; continue
            elif grid[x][y] == '-':
                y += 1; continue
            elif grid[x][y] == '+':
                if x < len(grid)-1 and grid[x+1][y] == '|':
                    x += 1; dir = 'D'; continue
                elif x > 0 and grid[x-1][y] == '|':
                    x -= 1; dir = 'U'; continue 
            else:
                walk.append(grid[x][y])
                y += 1; continue

        elif dir == 'L':
            if grid[x][y] == '|':
                y -= 1; continue
            elif grid[x][y] == '-':
                y -= 1; continue
            elif grid[x][y] == '+':
                if x < len(grid)-1 and grid[x+1][y] == '|':
                    x += 1; dir = 'D'; continue 
                elif x > 0 and grid[x-1][y] == '|':
                    x -= 1; dir = 'U'; continue 
            else:
                walk.append(grid[x][y])
                y -= 1; continue


with open('day19_input.txt','r') as file:
    grid = []
    i = 0
    for row in file.readlines():
        sym = list(row.strip('\n'))
        grid.append([])
        for j in range(len(sym)):
            grid[i].append(sym[j])
        i += 1

#try:
    walk_grid(grid, 'D', 0, grid[0].index('|'))
#except:
#    print('Solution1: ',walk)