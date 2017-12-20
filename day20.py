from operator import add
from collections import defaultdict

def parse_data(data):
    cln = data[3:].strip('>\n')
    crds = cln.split(',')
    return [int(x) for x in crds]

with open('day20_input.txt', 'r') as file:
    particles = []
    for row in file.readlines():
        data = row.split(', ')
        prt = []
        for d in data:
            prt.append(parse_data(d))
        particles.append(prt)

idx = 0
while(idx < 1000):
    idx += 1
    distances = []
    collisions = defaultdict(list)

    for i in range(len(particles)):
        particles[i][1] = list(map(add, particles[i][1], particles[i][2]))
        particles[i][0] = list(map(add, particles[i][0], particles[i][1]))
        distances.append(sum([abs(x) for x in particles[i][0]]))
        hsh = (particles[i][0][0],particles[i][0][1],particles[i][0][2])
        #print(hsh)
        collisions[hsh].append(particles[i])

    for col in collisions.values():
        if len(col) > 1:
            for dupicle in col:
                particles.remove(dupicle)

    #print(len(particles))

print(len(particles))
#print(distances.index(min(distances)))

