from collections import defaultdict

def countvalid(fnc):
    with open('day04_input.txt', 'r') as file:
        count1 = 0
        for row in file.readlines():
            words = defaultdict(int)
            isrowvalid = True
            for word in row.split():
                word = ''.join(fnc(word))
                if words[word] == 0:
                    words[word] = 1
                else:
                    isrowvalid = False
            if isrowvalid:
                count1 += 1
    print("Solution: ",count1)

countvalid(lambda x: x)
countvalid(sorted)