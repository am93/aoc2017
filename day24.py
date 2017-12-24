from collections import defaultdict

max_len = -1
max_val = -1

def make_bridge(parts, used, crr):
    global max_val
    global max_len
    any_new = False
    for p in parts:
        if used[p] > 0:
            continue
        elif p[0] == crr:
            any_new = True
            n_used = used.copy()
            n_used[p] = 1
            make_bridge(parts, n_used, p[1])
        elif p[1] == crr:
            any_new = True
            n_used = used.copy()
            n_used[p] = 1
            make_bridge(parts, n_used, p[0])

    if not any_new:
        crr_sum = 0
        cnt = 0
        for key in used.keys():
            if used[key] == 1:
                cnt += 1
                crr_sum += (key[0]+key[1])
        if cnt >= max_len and crr_sum > max_val:
            max_val = crr_sum
            max_len = cnt
        
with open('day24_input.txt', 'r') as file:
    parts = []
    for row in file.readlines():
        data = [int(x) for x in row.strip('\n').split('/')]
        parts.append(tuple(data))

    used = defaultdict(int)
    make_bridge(parts, used, 0)
    print(max_val)

    
