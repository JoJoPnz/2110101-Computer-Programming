import numpy as np


def to_cluster(a):
    """
    Seperate cluster from 2d array.

    # Parameters
    a: array_like - 2 dimension array of `True` or `False` with dtype np.bool.

    # Returns
    cluster_list: List - a list of 2d array each with only one cluster.

    # Notes
    This function doesn't guarantee order of output.

    # Examples
    >>> a = np.array([
                [1, 0, 1],
                [1, 0, 1],
                [1, 0, 1],
            ], np.bool)
    >>> np.array(to_cluster(a))
    array([[[ True, False, False],
            [ True, False, False],
            [ True, False, False]],
           [[False, False,  True],
            [False, False,  True],
            [False, False,  True]]])
    """
    height, width = a.shape
    output = []
    last_cross_section = []
    start_row = np.argmax(np.pad(np.max(a, axis=1), ((0, 1),), mode='constant', constant_values=np.inf))
    for row_index in range(start_row, height):
        cross_section = []
        seg_start = np.argmax(np.pad(a[row_index], ((0, 1),), mode='constant', constant_values=np.inf))
        for col_index in range(seg_start, width + 1):
            if (col_index == width and a[row_index][col_index-1]) or (col_index < width and a[row_index][col_index-1] and not a[row_index][col_index]):
                seg = np.full_like(a, False)
                seg[row_index, seg_start:col_index] = True
                cross_section.append(seg)
            if col_index < width and not a[row_index][col_index-1] and a[row_index][col_index]:
                seg_start = col_index
        marked_remove = set()
        for lcs in last_cross_section:
            merged_to = None
            for ic, ccs in enumerate(cross_section):
                if np.any(np.logical_and(lcs[row_index - 1], ccs[row_index])):
                    if merged_to is None:
                        ccs[:, :] = np.logical_or(lcs, ccs)  # inplace merge
                        merged_to = ccs
                    else:  # merge into the same lcs, so need to remove from last_cross_section
                        merged_to[:, :] = np.logical_or(merged_to, ccs)  # inplace merge
                        marked_remove.add(ic)
            if merged_to is None:
                output.append(lcs)
        last_cross_section = [cross_section[ic] for ic in range(len(cross_section)) if ic not in marked_remove]
    output.extend(last_cross_section)
    return output

#-----------------------------------------------------------------#
method = input()
W,L,H = [int(e) for e in input().split(',')]
data = []
data2 = []
for i in range(H):
    a = np.ndarray((L,W),np.bool)
    for j in range(L):
        b = input()
        for e in range(len(b)):
            if b[e] == 'x':
                b = b[:e] + '1' + b[e+1:]
            elif b[e] == '-':
                b = b[:e] + '0' + b[e+1:]
        for k in range(W):
            a[j,k] = int(b[k])
    #to_cluster(a)
    data.append(to_cluster(a)) # list = [ [numpy,numpy] , [numpy,numpy] ]
    data2.append(a)

#---check island---#
haveisland = False
support = 'M'
outy = []
outn = []
for i in range(1,H): #floor
    for e in data[i]:
        block = []
        z = np.where(e == True)
        z0 = z[0].tolist()
        z1 = z[1].tolist()
        for j in range(len(z0)):
            block.append([z0[j],z1[j]])
            
        Thisgroupis_island = True
        for r,c in block:
            if data2[i-1][r,c] == True:
                Thisgroupis_island = False
                break
            
        if Thisgroupis_island:
            for r,c in block:
                if data2[i-1][r,c] == False:
                    haveisland = True
                    for k in range(i-2,-1,-1): # previous floor
                        if data2[k][r,c] == True:
                            support = 'I'
                            break
                    outn.append([i,r,c])
                    outy.append([i,support,r,c])
                    support = 'M'
                    
outn.sort()
outy.sort()
if not haveisland:
    print('There is no island')
else:
    if method == 'N':
        realn = []
        for i,r,c in outn:
            realn.append([str(i),str(r),str(c)])
        for e in realn:
            print(','.join(e))
    elif method == 'Y':
        realy = []
        for i,sup,r,c in outy:
            realy.append([str(i),sup,str(r),str(c)])
        for e in realy:
            print(','.join(e))

