from collections import defaultdict

def parse_state(tape, idx, state):
    if state == 'A':
        if tape[idx] == 0:
            tape[idx] = 1
            idx += 1
            state = 'B'
        else:
            tape[idx] = 0
            idx -= 1
            state = 'F'
    elif state == 'B':
        if tape[idx] == 0:
            tape[idx] = 0
            idx += 1
            state = 'C'
        else:
            tape[idx] = 0
            idx += 1
            state = 'D'
    elif state == 'C':
        if tape[idx] == 0:
            tape[idx] = 1
            idx -= 1
            state = 'D'
        else:
            tape[idx] = 1
            idx += 1
            state = 'E'
    elif state == 'D':
        if tape[idx] == 0:
            tape[idx] = 0
            idx -= 1
            state = 'E'
        else:
            tape[idx] = 0
            idx -= 1
            state = 'D'
    elif state == 'E':
        if tape[idx] == 0:
            tape[idx] = 0
            idx += 1
            state = 'A'
        else:
            tape[idx] = 1
            idx += 1
            state = 'C'
    elif state == 'F':
        if tape[idx] == 0:
            tape[idx] = 1
            idx -= 1
            state = 'A'
        else:
            tape[idx] = 1
            idx += 1
            state = 'A'
    return (tape, idx, state) 

tape = defaultdict(int)
idx = 0
cnt = 0
state = 'A'

while(cnt < 12994925):
    cnt += 1
    (tape, idx, state) = parse_state(tape,idx,state)

print(sum([tape[key] for key in tape.keys()]))