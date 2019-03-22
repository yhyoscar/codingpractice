# implement of bubble sort, selection sort, merge sort, quick sort, heap sort, and bucket sort

def bubblesort(array):
    n = len(array)
    flag = True
    while flag:
        flag = False
        for i in range(n-1):
            if array[i] > array[i+1]:
                tmp = array[i]
                array[i] = array[i+1]
                array[i+1] = tmp
                flag = True
    return

def selectsort(array):
    n = len(array)
    for i in range(n-1):
        im = i
        for j in range(i+1, n):
            if array[j] < array[im]: im = j
        if im > i:
            tmp = array[i]
            array[i] = array[im]
            array[im] = tmp
    return

def merging(a, b):
    c = []
    i = 0; j = 0; na = len(a); nb = len(b)
    while i<na and j<nb:
        if a[i] < b[j]: 
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i == na: c.extend(b[j:])
    if j == nb: c.extend(a[i:])
    return c
    
def mergesort(array):
    n = len(array)
    m = 2
    while m<n:
        for i in range(n//m+1):
            array[i*m:(i+1)*m] = merging(array[i*m:int(i*m+m/2)], array[int(i*m+m/2):(i+1)*m])
        m *= 2
    return

def quicksort(array):
    # 1. build a partition binary tree by using the last element as pivot
    # 2. traverse the tree with in-order
    root = partition(array)
    return traverse_inorder(root)

def partition(array):
    if len(array) > 0:
        node = {'value':array[-1], 'left':None, 'right':None}
        left = []; right = []
        for e in array[:-1]:
            if e < node['value']:
                left.append(e)
            else:
                right.append(e)
        node['left'] = partition(left)
        node['right'] = partition(right)
    else:
        node = None
    return node

def traverse_inorder(node):
    array = []
    if node is not None:
        array = traverse_inorder(node['left'])
        array.append(node['value'])
        array.extend(traverse_inorder(node['right']))
    return array


if __name__ == '__main__':
    array = [4,5,8,6,7,2,3,1,9]
    bubblesort(array)
    print(array)
    array = [4,5,8,6,7,2,3,1,9]
    selectsort(array)
    print(array)
    array = [4,5,8,6,7,2,3,1,9]
    mergesort(array)
    print(array)
    array = [8,3,2,4,1,5,7,6]
    print( quicksort(array) )




