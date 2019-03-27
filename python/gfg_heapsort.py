
def heapify(array, n, i):
    if i<n:
        imax = i
        ileft = 2*i + 1
        iright= 2*i + 2
        if ileft<n and array[ileft]>array[imax]:
            imax = ileft
        if iright<n and array[iright]>array[imax]:
            imax = iright
        if imax!=i:
            array[i], array[imax] = array[imax], array[i]
            return heapify(array, n, imax)
        return i
    else:
        return i

def heapsort(array):
    n = len(array)
    for i in range(n)[::-1]:
        print(i, array, array[i])
        print(heapify(array, n, i))
    for i in range(1,n)[::-1]:
        print(i)
        print(array)
        array[0], array[i] = array[i], array[0]
        heapify(array, i, 0)
    return

array = [ 6,5,3,1,8,7,2,4]
heapsort(array)
print(array)
