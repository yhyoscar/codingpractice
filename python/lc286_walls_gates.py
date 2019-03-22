# LeetCode 286 - Walls and Gates
import numpy as np

def mindistance(field):
    nrow = len(field); ncol = len(field[0])
    for i in range(nrow):
        if field[i][0] == 0:
            print(i, 0)
            mindist_BFS(field, i, 0)
            for x in field: print(x)

    for i in range(nrow):
        if field[i][ncol-1] == 0:
            print(i, ncol-1)
            mindist_BFS(field, i, ncol-1)
            for x in field: print(x)

    for j in range(1,ncol-1):
        if field[0][j] == 0:
            print(0, j)
            mindist_BFS(field, 0, j)
            for x in field: print(x)

    for j in range(1,ncol-1):
        if field[nrow-1][j] == 0:
            print(nrow-1, j)
            mindist_BFS(field, nrow-1, j)
            for x in field: print(x)
            
    return 

def mindist_BFS(field, i0, j0):
    nrow = len(field); ncol = len(field[0])
    queue = [[i0,j0,0]]
    while len(queue)>0:
        loc = queue.pop(0)
        i=loc[0]; j=loc[1]
        if i-1>=0 and loc[2]+1<field[i-1][j]:
            field[i-1][j] = loc[2]+1
            queue.append([i-1,j,loc[2]+1])
        if i+1<nrow and loc[2]+1<field[i+1][j]:
            field[i+1][j] = loc[2]+1
            queue.append([i+1,j,loc[2]+1])
        if j-1>=0 and loc[2]+1<field[i][j-1]:
            field[i][j-1] = loc[2]+1
            queue.append([i,j-1,loc[2]+1])
        if j+1<ncol and loc[2]+1<field[i][j+1]:
            field[i][j+1] = loc[2]+1
            queue.append([i,j+1,loc[2]+1])
    return        

e = np.inf
field= [[e, -1,  0,  e, 0], 
        [e,  e,  e, -1, e], 
        [e, -1,  e, -1, e], 
        [0, -1,  e,  e, e]]

mindistance(field)
    
