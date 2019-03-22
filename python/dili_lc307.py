import numpy as np

def build_segment_tree(array, start, end, tree, inode):
    if start == end:
        tree[inode] = array[start]
    else:
        #print(inode, start, end)
        mid = int((start+end)/2)
        build_segment_tree(array, start, mid, tree, inode*2)
        build_segment_tree(array, mid+1, end, tree, inode*2+1)
        tree[inode] = tree[inode*2] + tree[inode*2+1]
    return


def update(array, start, end, tree, inode, k, diff):
    if start == end:
        tree[inode] += diff
        array[k] += diff
    else:
        mid = int((start+end)/2)
        if  start<=k<=mid:
            update(array, start, mid, tree, inode*2, k, diff)
        else:
            update(array, mid+1, end, tree, inode*2+1, k, diff)
        tree[inode] = tree[inode*2] + tree[inode*2+1]
    return

def subsum(array, start, end, tree, inode, left, right):
    if left<=start and right >= end:
        return tree[inode]
    if left>end or right<start:
        return 0
    else:
        mid = int((start+end)/2)
        sleft = subsum(array, start, mid, tree, inode*2, left, right)
        sright = subsum(array, mid+1, end, tree, inode*2+1, left, right)
        return sleft + sright




for k in range(10, 11):
    array = list(range(k))
    print(array)
    nlayer = int(np.ceil(np.log(k)/np.log(2)))+1
    tree = [None for i in  range(2**nlayer)]
    build_segment_tree(array, 0, len(array)-1, tree, 1)
    print(k, tree)

    update(array, 0, len(array)-1, tree, 1, 0, 9)
    print(k, tree)
    print(array)

    print(subsum(array, 0, len(array)-1, tree, 1, 1, 9))

