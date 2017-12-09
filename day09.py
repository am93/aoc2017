def process(data):
    score = 0
    depth = 1
    removed = 0
    garbage_mode = False
    ignore = False

    for c in data:
        if not ignore and garbage_mode and c == '!':
            ignore = True
            continue
        elif garbage_mode and ignore:
            ignore = False
            continue
        elif garbage_mode and c == '>':
            garbage_mode = False
            continue
        elif not garbage_mode and c == '<':
            garbage_mode = True
            continue
        elif garbage_mode:
            removed += 1
            continue
        elif c == '{': 
            score += depth
            depth += 1
        elif c == '}':
            depth -= 1
    return (score, removed)


with open('day09_input.txt') as file:
    print(process(file.readline()))
