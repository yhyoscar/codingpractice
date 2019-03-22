# Write a method to compute all permutations of a string.

# Recursion: p(n) = n*p(n-1)
def permutation(s):
    plist = []
    n = len(s)
    if n == 0:
        return None
    else:
        permutation_recur(s, n, plist)
        return plist

def permutation_recur(s, n, plist):
    if n==1:
        plist.append(s[0])
    else:
        permutation_recur(s, n-1, plist)
        nplist = len(plist)
        for j in range(nplist):
            p = plist[j]
            plist[j] =  p + s[n-1]
            for i in range(n-1):
                plist.append(p[:i]+s[n-1]+p[i:])
    return

if __name__ == '__main__':
    plist = permutation('abcd')
    for p in plist:
        print(p)


