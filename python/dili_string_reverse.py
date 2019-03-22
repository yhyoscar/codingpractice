

def rev(string):
    slist = list(string)
    low = 0; high = len(string)-1
    while low < high:
        tmp = slist[low]
        slist[low] = slist[high]
        slist[high] = tmp
        low += 1
        high -= 1
    return ''.join(slist)

print(rev('English'))

