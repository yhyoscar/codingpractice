# Find a triplet a, b, c such that a2 = b2 + c2. Variations of this problem like find a triplet with sum equal to 0. Find a pair with given sum. All such questions are efficiently solved using hashing.

# Given an array of integers, write a function that returns true if there is a triplet (a, b, c) that satisfies a2 + b2 = c2.

import numpy as np

def find_triplet(array):
    sa = sorted(np.array(array)**2)
    for i in range(len(array)-1, 1, -1):
        for j in range(i-1):
            if sa[i]-sa[j] in sa[0:i]:
                return np.sqrt(sa[i]), np.sqrt(sa[j]), np.sqrt(sa[i]-sa[j])
 
if __name__ == '__main__':
    print(find_triplet([1,2,3,4,5]))

