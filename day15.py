def generatorA():
    x = 699
    while True:
        x *= 16807
        x %= 2147483647
        if x % 4 == 0:
            yield x

def generatorB():
    x = 124
    while True:
        x *= 48271
        x %= 2147483647
        if x % 8 == 0:
            yield x

matches = 0
genA = generatorA()
genB = generatorB()
for i in range(5000000):
    if next(genA) & 0xFFFF == next(genB) & 0xFFFF:
        matches += 1

print(matches)