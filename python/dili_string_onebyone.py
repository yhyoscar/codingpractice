
from collections import defaultdict

def findtop(freq, clist):
    top = 0; c = ''
    for x in clist:
        if freq[x] > top:
            c = x
            top = freq[x]
    return c, top

def reorder(string):
    freq = defaultdict(lambda: 0)
    for c in string:
        freq[c] += 1
    ctop, ftop = findtop(freq, freq.keys()) 
    if len(string)//ftop >= 2:
        sout = ctop
        freq[ctop] -= 1
        for i in range(len(string)-1):
            clist = list(freq.keys())
            clist.remove(sout[-1])
            ctop, ftop = findtop(freq, clist=clist)
            sout += ctop
            freq[ctop] -= 1
        return sout
    else:
        return 'FALSE'

print(reorder('aaaaabbc'))

