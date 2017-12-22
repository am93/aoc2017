import numpy as np 

def process_sbmtrx(sbmtrx, matching):
    for key in matching.keys():
        m = np.matrix(key)
        #print(m)
        if not m.shape == sbmtrx.shape:
            continue
        if (sbmtrx == m).all():
            return matching[key]
        if (sbmtrx == np.flip(m,0)).all():
            return matching[key]
        if (sbmtrx == np.flip(m,1)).all():
            return matching[key]
        if (sbmtrx == np.rot90(m,k=1)).all():
            return matching[key]
        if (sbmtrx == np.rot90(m,k=2)).all():
            return matching[key]
        if (sbmtrx == np.rot90(m,k=3)).all():
            return matching[key]
        if (sbmtrx == np.rot90(np.flip(m,0),k=1)).all():
            return matching[key]
        if (sbmtrx == np.rot90(np.flip(m,0),k=2)).all():
            return matching[key]
        if (sbmtrx == np.rot90(np.flip(m,0),k=3)).all():
            return matching[key]
        if (sbmtrx == np.rot90(np.flip(m,1),k=1)).all():
            return matching[key]
        if (sbmtrx == np.rot90(np.flip(m,1),k=2)).all():
            return matching[key]
        if (sbmtrx == np.rot90(np.flip(m,1),k=3)).all():
            return matching[key]
    print('No match found !!!')
    return None

mtrx = np.matrix('0 1 0; 0 0 1; 1 1 1')
matching_rules = {}

with open('day21_input.txt', 'r') as file:
    for row in file.readlines():
        data = row.split(' => ')
        d_i = data[0].replace('.','0 ').replace('#','1 ').replace('/','; ')
        d_o = np.matrix(data[1].replace('.','0 ').replace('#','1 ').replace('/','; '))
        matching_rules[d_i] = d_o

steps = 0
while steps < 18:
    steps += 1
    print(steps)
    (x,_) = mtrx.shape

    subsize = -1
    if x % 2 == 0:
        subsize = 2
    else:
        subsize = 3

    
    # vrstice
    v_tmp = None
    for i in range(0,x,subsize):
        # stolpci
        h_tmp = None
        for j in range(0,x,subsize):
            sbmtrx = mtrx[i:i+subsize,j:j+subsize]
            tmp = process_sbmtrx(sbmtrx, matching_rules)
            #print(tmp)

            if h_tmp is None:
                h_tmp = tmp
            else:
                h_tmp = np.concatenate((h_tmp, tmp), axis=1)
                    
        if v_tmp is None:
            v_tmp = h_tmp
        else:
            v_tmp = np.concatenate((v_tmp, h_tmp), axis=0)

    mtrx = v_tmp

print(np.sum(mtrx))