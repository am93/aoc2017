from collections import defaultdict
import operator

registers = defaultdict(int)
operators = {'>': operator.gt, '<': operator.lt,
           '>=': operator.ge, '<=': operator.le,
           '==': operator.eq, '!=': operator.ne,
           'inc': operator.add, 'dec': operator.sub}

highest_ever = -9999999

with open('day08_input.txt', 'r') as file:
    for row in file.readlines():
        data = row.split()
        if operators[data[5]](registers[data[4]],int(data[6])):
            registers[data[0]] = operators[data[1]](registers[data[0]], int(data[2]))
            if highest_ever < registers[data[0]]:
                highest_ever = registers[data[0]]

max_val = -100000000
max_key = ''
for key in registers.keys():
    if registers[key] > max_val:
        max_val = registers[key]
        max_key = key

print('Solution: ',key,' ', max_val)
print('Solution2: ',highest_ever)