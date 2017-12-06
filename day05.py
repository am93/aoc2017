offsets = []
with open('day05_input.txt', 'r') as file:
    for row in file.readlines():
        offsets += [int(row)]

idx = 0
steps = 0
while(True):
    old_idx = idx
    idx += offsets[idx]
    offsets[old_idx] += 1
    steps += 1
    if idx >= len(offsets):
        print('Solution: ',steps)
        break

offsets = []
with open('input2.txt', 'r') as file:
    for row in file.readlines():
        offsets += [int(row)]
idx = 0
steps = 0
while(True):
    old_idx = idx
    idx += offsets[idx]
    if offsets[old_idx] >= 3:
        offsets[old_idx] -= 1
    else:
        offsets[old_idx] += 1
    steps += 1
    if idx >= len(offsets):
        print('Solution2: ',steps)
        break