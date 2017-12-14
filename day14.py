from day10 import knothash
from collections import defaultdict

input_val = 'nbysizxe'

def to_bits(val):
    bits = ['','','','']
    for x in range(3,-1,-1):
        bits[x] = str(val % 2)
        val = int(val/2)
    return ''.join(bits)

def store_disk(disk, bits, row):
    for (i,b) in enumerate(bits):
        disk[row,i] = b
    return disk

def generate_moves(x,y):
    moves = set()
    moves.add((x+1,y)); moves.add((x-1,y))
    moves.add((x,y+1)); moves.add((x,y-1))
    return moves

def find_connected(disk, cands, key):
    if len(cands) == 0:
        return disk
    else:
        (x,y) = cands.pop()
        if disk[x,y] == 1:
            disk[x,y] = key
            cands = cands.union(generate_moves(x,y))
        return find_connected(disk, cands, key)

result1 = 0
disk = defaultdict(lambda: -1)

for x in range(128):
    key = input_val+'-'+str(x)
    vals = [int(x,16) for x in knothash(key)]
    bits = ''.join([to_bits(v) for v in vals])
    bv = [int(x) for x in bits]
    disk = store_disk(disk, bv, x)
    result1 += sum(bv)

print('Solution1: ',result1)

key = 1
cands = set()
for x in range(128):
    for y in range(128):
        if not disk[x,y] == 1:
            continue
        else:
            key += 1
            cands.add((x,y))
            disk = find_connected(disk, cands, key)


print('Solution2: ', key-1)