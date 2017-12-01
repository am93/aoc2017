sum1,sum2 = 0, 0
with open('day01_input.txt', 'r') as f:
    text = f.read()
    dist1 = 1
    dist2 = int(len(text) / 2)
    for x in range(0, len(text)):
        if text[x] == text[(x+dist1)%len(text)]:
            sum1 += int(text[x])
        if text[x] == text[(x+dist2)%len(text)]:
            sum2 += int(text[x])

print("Second solution: "+str(sum1))
print("Second solution: "+str(sum2))