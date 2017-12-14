from collections import defaultdict

tree = defaultdict(list)

def parse_row(row):
    data = row.split('->')
    source = data[0].split()[0]
    weight = int(data[0].split()[1][1:-1])
    tree[source] = [weight,[]]
    if len(data) > 1:
        childs = data[1].split(', ')
        childs = [c.strip() for c in childs]
        tree[source][1] = childs  

def iterate_tree(key):
    count = 1
    for c in tree[key][1]:
        count += iterate_tree(c)
    return count

def sum_weight(key):
    weight = tree[key][0]
    for c in tree[key][1]:
        weight += sum_weight(c)
    return weight

def weight_tree(key):
    weights =  []
    for c in tree[key][1]:
        weights += [sum_weight(c)]
    return weights

def check_weights(key):
    weights = weight_tree(key)
    for c in tree[key][1]:
        check_weights(c)
        if len(weights) > 0 and not all(weights[0] == e for e in weights):
            print(weights)
            print(tree[key][1])
        

with open('day07_input.txt', 'r') as file:
    for row in file.readlines():
        parse_row(row)

    root = ''

    for x in tree.keys():
        count = iterate_tree(x)
        if count == len(tree.keys()):
            print('Root: ',x)
            root = x
            break
    
    check_weights(root)
    print(tree['lnpuarm'][0])
    print(weight_tree('lnpuarm'))
    print


    
