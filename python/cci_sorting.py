
def tower(hwlist):
    slist = sorted(hwlist, key=lambda t: t[0], reverse=False)
    maxlen = [1 for i in slist]
    pre    = [None for i in slist]

    for i in range(1,len(slist)):
        for j in range(i):
            if slist[i][1] > slist[j][1] and maxlen[i] < maxlen[j]+1:
                maxlen[i] = maxlen[j]+1
                pre[i] = j
    print(maxlen)
    print(pre)
    loc = maxlen.index(max(maxlen))
    while pre[loc] is not None:
        print(slist[loc], end=' -> ')
        loc = pre[loc]
    print(slist[loc])

    return slist


hwlist = [(65, 100), (70, 190), (56, 90), (75, 120), (76, 130), (78, 140), (60, 85), (68, 160), (80, 120)]
print(tower(hwlist))


