from collections import defaultdict

mul_count = 0

def get_value(val, regs):
    if len(val) == 1 and val.isalpha():
        return regs[val]
    else:
        return int(val)

def parse_instr(instrs, idx, regs):
    global mul_count
    add = True
    instr = instrs[idx]
    if instr[0] == 'set':
        regs[instr[1]] = get_value(instr[2],regs)
    elif instr[0] == 'sub':
        regs[instr[1]] -= get_value(instr[2],regs)
    elif instr[0] == 'mul':
        regs[instr[1]] *= get_value(instr[2],regs)
        mul_count += 1
    elif instr[0] == 'jnz':
        x = get_value(instr[1], regs)
        y = get_value(instr[2], regs)
        if not x == 0:
            idx += y
            add = False
    
    if add: idx += 1
    return (regs, idx)
    
with open('day23_input.txt', 'r') as file:
    
    instrs = []
    for row in file.readlines():
        data = row.split()
        instrs.append(data)

    regs = defaultdict(int)
    #regs['a'] = 1
    idx = 0
    stop_exec = False
    while(not stop_exec):
        if idx == len(instrs):
            break
        else:
            (regs, idx) = parse_instr(instrs, idx, regs)

    print(mul_count)

h = 0
for x in range(109900,126900 + 1,17):
    for i in range(2,x):
        if x % i == 0:
            h += 1
            break