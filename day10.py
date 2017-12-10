def to_ascii_arr(data):
    tmp = []
    for c in data:
        if c == ',': tmp.append(44)
        elif c == ' ': tmp.append(32)
        else: tmp.append(48+int(c))
    tmp += [17,31,73,47,23]
    return tmp

def process(arr, idx, skip, l):
    tmp = []
    for i in range(idx,idx+l):
        t_idx = i % len(arr)
        tmp.append(arr[t_idx])
    tmp.reverse()
    for i in range(idx,idx+l):
        t_idx = i % len(arr)
        arr[t_idx] = tmp[i-idx]
    idx = (idx + l + skip) % 256
    skip += 1
    return (arr, idx, skip)

lens1 = '130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224'.split(',')
lens2 = to_ascii_arr('130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224')
arr = list(range(0,256))
skip = 0
idx = 0
for _ in range(64):
    for l in lens2:
        l = int(l)
        (arr, idx, skip) = process(arr, idx, skip, l)
    #print('Solution1: ',arr[0]*arr[1])

hidx = 0
hashes = []
while(hidx < 255):
    tmp = 0
    for i in range(16):
        tmp = tmp ^ arr[hidx+i]
    hashes.append(tmp)
    hidx += 16

sol = []
for x in hashes:
    y = hex(x).split('x')[1]
    if len(y) == 1: y += '0'
    sol.append(y)
print('Solution2: ',''.join(sol))

