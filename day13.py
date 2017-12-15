from collections import defaultdict

def move_sentries(sentry, firewall, length, directions):
    for i in range(length):
        if sentry[i] == -1: continue
        sentry[i] += directions[i]
        if sentry[i] == firewall[i] - 1:
            directions[i] = -1
        elif sentry[i] == 0:
            directions[i] = 1
    return sentry

firewall = defaultdict(int)
sentry = defaultdict(lambda: -1)
directions = defaultdict(lambda: 1)
length = -1
with open('day13_input.txt', 'r') as file:
    for row in file.readlines():
        data = row.split(':')
        idx = int(data[0].strip())
        firewall[idx] = int(data[1].strip())
        sentry[idx] = 0
        length = idx+1

severity = 0
delay = 0
inital_state = sentry.copy()
inital_dir = directions.copy()

while(True):
    delay += 1
    sentry = inital_state.copy()
    directions = inital_dir.copy()
    detected = False
    for _ in range(delay):
        move_sentries(sentry, firewall, length, directions)

    for i in range(length):
        if(sentry[i] == 0):
            severity += i*firewall[i]
            detected = True
            break
        sentry = move_sentries(sentry,firewall, length, directions)

    if not detected:
        print('Solution2: ', delay)
        break

print('Solution 1:', severity)