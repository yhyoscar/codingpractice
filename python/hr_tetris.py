
tetris = {1: [[1]], 
          2: [[2,0], 
              [2,2]], 
          3: [[0,3,0], 
              [3,3,3]],
          4: [[4,4,0], 
              [0,4,4]]
          }

w=6; h=6;
pieces=[
    [(0, 0), (1, 0), (2, 0), (3, 0)],
    [(0, 0), (1, 0), (2, 0), (2, 1)],
    [(0, 0), (1, 0), (0, 1), (1, 1)],
    [(0, 0), (1, 0), (0, 1), (2, 0)],

    [(0, 0), (1, 0), (2, 0), (2, -1)],
    [(0, 0), (1, 0), (1, -1), (2, -1)],
    [(0, 0), (1, 0), (1, -1), (2, -1)],
    [(0, 0), (1, 0), (1, -1), (1, -2)],
    [(0, 0), (1, 0), (1, 1), (0, 1)],
]


def tetris_matrix(pieces):
    n = len(pieces)
    tiles = {}; ava = {}
    for i in range(n):
        maxx = -999; maxy = -999; minx = 999; miny = 999
        for loc in pieces[i]:
           maxx = max(maxx, loc[0]+1)
           maxy = max(maxy, loc[1]+1)
           minx = min(minx, loc[0]+1)
           miny = min(miny, loc[1]+1)
        tiles[i] = [[-1 for i in range(maxx-minx+1)] for j in range(maxy-miny+1)]
    for i in range(n):
        ava[i] = 1
        for loc in pieces[i]:
            my = len(tiles[i])
            tiles[i][my-loc[1]-1][loc[0]] = i
    print(tiles)
    return tiles, ava


def check_fit(matrix, tile, loc):
    my = len(matrix); mx = len(matrix[0])
    ty = len(tile); tx = len(tile[0])
    new = [[matrix[i][j] for j in range(mx)] for i in range(my)]
    for k in range(len(tile[0])):
        if tile[0][k] >= 0: break
    if (loc[0]+ty>my) or (loc[1]-k<0) or (loc[1]+(tx-k)>mx):
        return False, 0
    else:
        for i in range(ty):
            for j in range(tx):
                if tile[i][j]>=0 and matrix[loc[0]+i][loc[1]-k+j]>=0:
                    return False, 0
        for i in range(ty):
            for j in range(tx):
                if tile[i][j] >= 0:
                    new[loc[0]+i][loc[1]-k+j] = tile[i][j]
        return True, new


def fit_tetris(matrix, tiles, ava, loc, solutions):
    m = len(matrix); n = len(matrix[0])
    if loc[1] >= n:
        if loc[0] >= n-1:
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] == -1: return
            solutions.append(matrix)
            return
        else:
            fit_tetris(matrix, tiles, ava, [loc[0]+1, 0], solutions)
    else:
        if matrix[loc[0]][loc[1]] > 0:
            fit_tetris(matrix, tiles, ava, [loc[0], loc[1]+1], solutions)
        else:
            for i in tiles:
                if ava[i] > 0:
                    print('-----------------')
                    for line in matrix:
                        print(line)
                    print('loc: ', loc)
                    print('tile: ', i, tiles[i])
                    flag, newmat = check_fit(matrix, tiles[i], loc)
                    print('flag: ', flag)
                    if flag:
                        avanew = {}
                        for k in ava:
                            avanew[k] = ava[k]
                        avanew[i] -= 1
                        fit_tetris(newmat, tiles, avanew, loc, solutions)
    return

def  pack_tetris(w, h, pieces):
    matrix = [[-1 for i in range(w)] for j in range(h)]
    tiles, ava = tetris_matrix(pieces)
    solutions = []
    fit_tetris(matrix, tiles, ava, [0, 0], solutions)
    print(solutions)
    for s in solutions:
        for line in s:
            print(line)
        print('=======================')
    return

pack_tetris(w, h, pieces)




