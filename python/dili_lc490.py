

def maze_bfs(array, start, target):
    
    nx = len(array[0]); ny = len(array)
    directions = [[1,0], [0,1], [-1, 0], [0, -1]]
    queue = [start]
    current = start
    while len(queue) > 0 and not (current[0] == target[0] and current[1] == target[1]):
        current = queue.pop(0)
        array[current[1]][current[0]] = 2
        print('----------------')
        print(current[::-1])
        for x in array:
            print(x)
        for d in directions:
            if (current[0]+d[0]<0) or (current[0]+d[0]>nx-1) or \
                    (current[1]+d[1]<0) or (current[1]+d[1]>ny-1) or \
                    array[current[1]+d[1]][current[0]+d[0]] > 0:
                continue
            else:
                queue.append([current[0]+d[0], current[1]+d[1]])
    return 

array = [[0,1,0,1], \
         [0,0,0,0], \
         [0,1,0,1]]
start = [0,0]
target = [3, 1]

maze_bfs(array, start, target)




