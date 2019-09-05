class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if len(matrix) == 0:
            return 0
        else:
            path = [[1 for j in x] for x in matrix]
            visited = [[False for j in x] for x in matrix]

            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    self.dfs(matrix, i, j, path, visited)

            #self.dfs(matrix, 1, 1, path, visited)   

            mp = 1
            for x in path:
                #print(x)
                mp = max(max(x), mp)            
            return mp
        
    def dfs(self, matrix, i, j, path, visited):
        if (0<=i<len(matrix)) and (0<=j<len(matrix[0])):
            #print(i, j, )
            if not visited[i][j]:
                tmp = []
                if i-1 >= 0 and matrix[i-1][j]>matrix[i][j]:
                    self.dfs(matrix, i-1, j, path, visited)
                    tmp.append( path[i-1][j] )
                if i+1 < len(matrix) and matrix[i+1][j]>matrix[i][j]:
                    self.dfs(matrix, i+1, j, path, visited)
                    tmp.append( path[i+1][j] )
                if j-1 >= 0 and matrix[i][j-1]>matrix[i][j]:
                    self.dfs(matrix, i, j-1, path, visited)
                    tmp.append( path[i][j-1] )
                if j+1 < len(matrix[0]) and matrix[i][j+1]>matrix[i][j]:
                    self.dfs(matrix, i, j+1, path, visited)
                    tmp.append( path[i][j+1] )
                if len(tmp) > 0:
                    path[i][j] = max(path[i][j], max(tmp) + 1)
                else:
                    path[i][j] = 1
                
                visited[i][j] = True
                


