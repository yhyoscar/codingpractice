# Given an square matrix, turn it by 90 degrees in anti-clockwise direction without using any extra space.


def rotate_matrix(mat, n):
    for icycle in range(n//2):
        for k in range(3):
            for m in range(n-2*icycle-1):
                if k == 0:
                    i1 = icycle
                    j1 = icycle + m
                    i2 = icycle + m
                    j2 = n-icycle-1
                if k == 1:
                    i1 = icycle + m
                    j1 = n-icycle-1
                    i2 = n-icycle-1
                    j2 = n-icycle-1-m
                if k == 2:
                    i1 = n-icycle-1
                    j1 = n-icycle-1-m
                    i2 = n-icycle-1-m
                    j2 = icycle
                tmp = mat[i1][j1]
                mat[i1][j1] = mat[i2][j2]
                mat[i2][j2] = tmp
    return mat

mat = [[1,2,3,4], [5,6,7,8], [9,10,11,12], [13,14,15,16]]
print(rotate_matrix(mat, 4))


