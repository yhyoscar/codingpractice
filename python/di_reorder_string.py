# Given a string, reorder the characters by their frequency
# Input: bloomberg, Output: bbooeglmr

from operator import itemgetter

def reorder(string):
    strs = []
    nums = []
    for c in string:
        if c in strs:
            nums[strs.index(c)] += 1
        else:
            strs.append(c)
            nums.append(1)
    tmp = [[strs[i], -nums[i]] for i in range(len(strs))]
    tmp = sorted(tmp, key=itemgetter(1,0), reverse=False )
    return ''.join([x[0]*(-x[1]) for x in tmp])
    
reorder('bloomberg')
