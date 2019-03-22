# Imagine a robot sitting on the upper left hand corner of an NxN grid. The robot can only move in two directions: right and down. How many possible paths are there for the robot?
# FOLLOW UP
# Imagine certain squares are “off limits”, such that the robot can not step on them. Design an algorithm to get all possible paths for the robot.

import numpy as np

# DP: restore the solution in a 2D array and recursively solve it
# Recursive equation: S(i,j) = S(i-1,j) + S(i,j-1); if (i,j) is available, else S(i,j) = 0
def robotwalk(grid):
    # grid(i,j) = False unavailable, True available
    n, m = grid.shape[0], grid.shape[1]
    s = np.zeros([n+1, m+1]).astype(int) 
    s[1:,1:] = -1
    robotwalk_recur(grid, s, n, m)
    print(s[1:,1:])
    return s[n, m]

def robotwalk_recur(grid, s, n, m):
    print(n, m)
    if grid[n-1, m-1]:
        if n==1 and m==1:
            s[1,1] = 1
            return
        if n>1 and grid[n-2,m-1] and s[n-1,m]<0:
            robotwalk_recur(grid, s, n-1, m)
        if m>1 and grid[n-1,m-2] and s[n,m-1]<0:
            robotwalk_recur(grid, s, n, m-1)
        s[n,m] = max(0, s[n-1,m]) + max(0, s[n,m-1])
    else:
        s[n,m] = 0
    return

if __name__ == '__main__':
    grid = np.zeros([3,4]) + True
    grid[1,:2] = False
    print( robotwalk(grid) )

