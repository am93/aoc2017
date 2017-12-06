from collections import defaultdict

with open('day06_input.txt', 'r') as file:
    values = [int(x) for x in file.readline().split()]
    seen = defaultdict(int)
    steps = 0
    while(True):
        idx = values.index(max(values))
        max_val = max(values)
        steps += 1
        values[idx] = 0
        while(max_val > 0):
            max_val -= 1
            idx += 1
            if idx > len(values)-1:
                idx = 0
            values[idx] += 1
        key = ''.join([str(x) for x in values])
        if seen[key] > 0:
            val = steps-seen[key]
            print('Loop size: ',val)
            break
        else:
            seen[key] = steps

print('Steps:',steps)

