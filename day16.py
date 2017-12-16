def dance(rps, chars, commands):
    cache = []
    for i in range(rps):
        tmp = ''.join(chars)
        if tmp in cache:  
            print('Cycle detected. Solution2: ',cache[rps % i])
            return
        cache.append(tmp)

        for comm in commands:
                if comm[0] == 's':
                    i = int(comm[1:])
                    chars = chars[-i:] + chars[:-i]
                elif comm[0] == 'x':
                    vals = [int(x) for x in comm[1:].split('/')]
                    first = chars[vals[0]]
                    second = chars[vals[1]]
                    chars[vals[0]] = second
                    chars[vals[1]] = first
                elif comm[0] == 'p':
                    vals = comm[1:].split('/')
                    idx1 = chars.index(vals[0])
                    idx2 = chars.index(vals[1])
                    first = chars[idx1]
                    second = chars[idx2]
                    chars[idx1] = second
                    chars[idx2] = first

    print('Solution: ',''.join(chars))


with open('day16_input.txt') as file:
    chars = [chr(97+i) for i in range(16)]
    commands = file.readline().split(',')
    seen = {}

    dance(1, chars[:], commands)
    dance(1000000000, chars[:], commands)