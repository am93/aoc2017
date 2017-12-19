from collections import defaultdict

snd_count = 0
locked = [False, False]
finished = [False, False]

def get_value(val, regs):
    if len(val) == 1 and val.isalpha():
        return regs[val]
    else:
        return int(val)

def parse_instr(instrs, idxs, regs2, queues, p_ind):
    global locked
    global snd_count
    idx = idxs[p_ind]
    regs = regs2[p_ind]
    instr = instrs[idx]
    old_idx = idx
    switch_program = False
    add = True
    if instr[0] == 'snd':
        queue[p_ind].append(get_value(instr[1], regs))
        locked[(p_ind+1)%2] = False
        if p_ind == 1: snd_count += 1
    elif instr[0] == 'set':
        regs[instr[1]] = get_value(instr[2],regs)
    elif instr[0] == 'add':
        regs[instr[1]] += get_value(instr[2],regs)
    elif instr[0] == 'mul':
        regs[instr[1]] *= get_value(instr[2],regs)
    elif instr[0] == 'mod':
        regs[instr[1]] = regs[instr[1]] % get_value(instr[2], regs)
    elif instr[0] == 'rcv':
        othr = (p_ind+1) % 2
        if len(queue[othr]) == 0:
            switch_program = True
            locked[p_ind] = True
            idx -= 1
            add = False
        else:
            regs[instr[1]] = queue[othr].pop(0)
    elif instr[0] == 'jgz':
        x = get_value(instr[1], regs)
        y = get_value(instr[2], regs)
        if x > 0:
            idx += y
            add = False
    
    if add: idx += 1
    idxs[p_ind] = idx
    regs2[p_ind] = regs
    return (regs2, idxs, queue, p_ind, switch_program)
    


with open('day18_input.txt', 'r') as file:
    
    instrs = []
    for row in file.readlines():
        data = row.split()
        instrs.append(data)

    regs = [defaultdict(int), defaultdict(int)]
    regs[0]['p'] = 0
    regs[1]['p'] = 1
    queue = [[],[]]
    idxs = [0,0]
    p_ind = 0
    stop_exec = False
    loop_cnt = 0
    while(not stop_exec):
        loop_cnt += 1
        if loop_cnt > 150000:
            print(idxs)
            print(snd_count)
            break
        #print(idxs)
        #print(instrs[idxs[p_ind]])
        if idxs[p_ind] == len(instrs):
            print(idxs)
            finished[p_ind] = True
            switch_program = True
        else:
            (regs2, idxs, queue, p_ind, switch_program) = parse_instr(instrs, idxs, regs, queue, p_ind)
        #print(p_ind, regs2, idxs)
        if switch_program:
            p_ind = (p_ind+1) % 2
            if finished[p_ind]:
                print(snd_count)
                break
        if locked[0] and locked[1]:
            print(snd_count)
            break