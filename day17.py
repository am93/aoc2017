buff = [0]
idx = 0
steps = 343

for i in range(1, 2018):
    idx = ((idx+steps)%len(buff))+1
    buff.insert(idx,i)

print('Solution1: ', buff[idx+1])

buff = [0]
idx = 0
steps = 343
solution = -1

for i in range(1, 50000001):
    idx = ((idx+steps)%len(buff))+1
    if idx == 1:
        solution = i
    buff.insert(idx,i)

print('Solution2: ', solution)