# Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents) and pennies (1 cent), write code to calculate the number of ways of representing n cents.

# DP: S(n,j) = S(n,j-1) + S(n-cent(j),j-1) + S(n-2*cent(j), j-1) + ...

import numpy as np

#  bottom-up approach
def cents_bottomup(n, changes = [1,5,10,25]):
    buf = np.zeros([n+1, len(changes)])
    buf[0,:] = 1
    buf[:,0][np.arange(n+1)%changes[0] == 0] = 1
    if len(changes) > 1:
        for j in range(1,len(changes)):
            for i in range(1, n+1):
                buf[i, j] = buf[i,j-1]
                for k in range(i//changes[j]):
                    buf[i,j] += buf[i-(k+1)*changes[j], j-1]
    print(buf)
    return buf[-1,-1]


if __name__ == '__main__':
    print(cents_bottomup(10, changes=[25,5,10,1]))


