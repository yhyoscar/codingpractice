# Write a method that returns all subsets of a set.

import copy

# Recursion: S(n) = 2*S(n-1)
def allsubsets(s):
    sublist = [[]]
    allsubsets_recur(s, sublist)
    for subset in sublist:
        print(subset)
    return

def allsubsets_recur(s, sublist):
    if len(s) == 1:
        sublist.append([s[0]])
    else:
        if len(s) > 1:
            allsubsets_recur(s[:-1], sublist)
            tmp = copy.deepcopy(sublist)
            for i in range(len(tmp)):
                tmp[i].append(s[-1])
            sublist.extend(tmp)
    return

if __name__ == '__main__':
    allsubsets([1,2,3,4])

