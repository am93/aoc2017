with open('day11_input.txt', 'r') as file:
    moves = file.readline().split(',')
    coord = [0, 0]
    furthest = 0
    for m in moves:
        if m == 'n':
            coord[0] += 1
        elif m == 'ne':
            coord[1] += 1
        elif m == 'nw':
            coord[1] -= 1
            coord[0] += 1
        elif m == 's':
            coord[0] -= 1
        elif m == 'se':
            coord[0] -= 1
            coord[1] += 1
        elif m == 'sw':
            coord[1] -= 1
        x = coord[0]
        z = coord[1]
        y = -x-z
        d = max(abs(x), abs(y), abs(z))
        furthest = max(d, furthest)
    print('Solution1: ',d)
    print('Solution2: ',furthest)