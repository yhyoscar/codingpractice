
def matmul(mat1, mat2):
    m1, n1 = len(mat1), len(mat1[0])
    m2, n2 = len(mat2), len(mat2[0])
    if n1 == m2:
        rm = [[0 for j in range(n2)] for i in range(m1)]
        for i in range(m1):
            for j in range(n1):
                for k in range(n2):
                    rm[i][k] += mat1[i][j]*mat2[j][k]
        return rm
    else:
        print('ERROR: size unmatched')
        return None


if __name__ == '__main__':

    mat1 = [[0.8, 0.1], 
            [0.2, 0.9]]
    mat2 = [[0.4], 
            [0.6]]
    for i in range(100):
        mat2 = matmul(mat1, mat2)
        print(i, mat2)

