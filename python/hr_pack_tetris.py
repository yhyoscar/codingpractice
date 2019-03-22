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
    tiles = {}
    for i in range(n):
        maxx = -999; maxy = -999; minx = 999; miny = 999
        for loc in pieces[i]:
           maxx = max(maxx, loc[0]+1)
           maxy = max(maxy, loc[1]+1)
           minx = min(minx, loc[0]+1)
           miny = min(miny, loc[1]+1)
        tiles[i] = [[0 for i in range(maxx-minx+1)] for j in range(maxy-miny+1)]
    for i in range(n):
        for loc in pieces[i]:
            tiles[i][loc[1]][loc[0]] = i
    print(tiles)
    return tiles


def check_fit(matrix, tile, tileid, loc):
    my = len(matrix); mx = len(matrix[0])
    nt = len(tile)
    new = [[matrix[i][j] for j in range(mx)] for i in range(my)]
    
    for e in tile:
        x = loc[1] + e[0]
        y = loc[0] + e[1]
        if x<0 or x>=mx or y<0 or y>=my:
            return False, 0
        else:
            if matrix[y][x] >= 0:
                return False, 0
            else:
                new[y][x] = tileid
    return True, new

# fit the tetris recurently
def fit_tetris(matrix, tiles, ava, loc, solutions):
    m = len(matrix); n = len(matrix[0])
    if loc[1] >= n:
        if loc[0] >= n-1:
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] < 0: return
            solutions.append(matrix)
            return
        else:
            fit_tetris(matrix, tiles, ava, [loc[0]+1, 0], solutions)
    else:
        if matrix[loc[0]][loc[1]] >= 0:
            fit_tetris(matrix, tiles, ava, [loc[0], loc[1]+1], solutions)
        else:
            for i in tiles.keys():
                if ava[i] > 0:
                    print('-----------------')
                    for line in matrix:
                        print(line)
                    print('loc: ', loc)
                    print('tile: ', i, tiles[i])
                    flag, newmat = check_fit(matrix, tiles[i], i, loc)
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
    tiles = {}; ava = {}
    for i in range(len(pieces)):
        tiles[i] = pieces[i]
        ava[i] = 1
    solutions = []
    fit_tetris(matrix, tiles, ava, [0, 0], solutions)
    for s in solutions:
        for line in s:
            print(line)
        print('=======================')
    return

tetris_matrix(pieces)
pack_tetris(w, h, pieces)



