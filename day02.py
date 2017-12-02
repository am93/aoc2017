sum = 0
with open('day02_input.txt', 'r') as file:
    for row in file.readlines():
        row = [int(x) for x in row.split()]
        sum += max(row) - min(row)

print('First solution: '+str(sum))

sum = 0
with open('day02_input.txt', 'r') as file:
    for row in file.readlines():
        row = [int(x) for x in row.split()]
        for x in range(0,len(row)-1):
            for y in range(x+1, len(row)):
                div = 0
                if row[x] > row[y]:
                    div = row[x] / row[y]
                else:
                    div = row[y] / row[x]
                if div.is_integer(): sum+=div

print('Second solution: '+str(sum))

# ----------------------------------------------------------------------------------------
# Code below this line is not mine - I found it on reddit and I really like the idea
# so I am keeping it in this file :)
import itertools

def digits(string):
    return [int(n) for n in string.split()]

with open('p02.txt') as fp:
    rows = [digits(line) for line in fp.read().strip().splitlines()]

print(sum(b-a for a, *_, b in map(sorted, rows)))
print(sum(b//a for row in rows for a, b in itertools.combinations(sorted(row), 2) if b%a==0))
