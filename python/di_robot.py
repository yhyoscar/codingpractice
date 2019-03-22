

class Robot:
    def __init__(self, x, y, direction):
        self.x = x
        self.y = y
        self.direction = direction

    def move(self, grid):
        ny = len(grid); nx = len(grid[0])
        if self.direction == 0:
            if self.x >= nx-1: return False
            if grid[self.y][self.x+1] != 1:  self.x += 1; return True
            else: return False
        if self.direction == 1:
            if self.y <= 0: return False
            if grid[self.y-1][self.x] != 1: self.y -= 1; return True
            else: return False
        if self.direction == 2:
            if self.x <= 0: return False
            if grid[self.y][self.x-1] != 1: self.x -= 1; return True
            else: return False
        if self.direction == 3:
            if self.y >= ny-1: return False
            if grid[self.y+1][self.x] != 1: self.y += 1; return True
            else: return False
    
    def turn_left(self):
        self.direction = (self.direction + 1) % 4
        return 

    def turn_right(self):
        self.direction = (self.direction - 1) % 4
        return

    def clean(self, grid):
        grid[self.y][self.x] = 2

def print_grid(grid):
    print('-----------------------')
    for line in grid:
        for x in line:
            print(format(x), end=' ')
        print('')
    print('-----------------------')
    return

def dfs(robot, grid):
    if grid[robot.y][robot.x]>0: return
    finished = True
    for row in grid:
        for x in row:
            if x == 0: finished = False
    if not finished:
        print_grid(grid)
        if grid[robot.y][robot.x]==0: 
            robot.clean(grid)
        for i in range(4):
            print('*** ',robot.y, robot.x, robot.direction, i, ' ***')
            flag = robot.move(grid)
            if flag: dfs(robot, grid)
            robot.turn_left()
            robot.turn_left()
            if flag: robot.move(grid)
            robot.turn_right()
    return

grid = [[0,0,0,0], 
        [0,0,1,1], 
        [1,0,0,0]]
robot = Robot(x=0, y=0, direction=0)
dfs(robot, grid)
print_grid(grid)


