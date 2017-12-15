from collections import defaultdict

with open('day12_input.txt', 'r') as file:
    graph = defaultdict(list)
    for row in file.readlines():
        vals = row.strip().split(' <-> ')
        node = int(vals[0])
        dests = map(lambda x: int(x.strip()), vals[1].split(','))
        #print(node, list(dests))
        for d in dests:
            graph[node].append(d)
            graph[d].append(node)

    
    visited = set()
    groups = 0
    for i in range(len(graph.keys())):
        if i in visited:
            continue

        groups += 1
        to_process = [i]

        while len(to_process) > 0:
            #print(to_process)
            x = to_process.pop()
            for node in graph[x]:
                if node not in visited:
                    visited.add(node)
                    to_process.append(node)

    #print('Solution1: ', len(visited))
    print('Solution2: ', groups)