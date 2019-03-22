class Solution:
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        nrow = len(matrix); ncol = len(matrix[0])
        if nrow==1 or ncol==1: return True
        else:
            for i in range(1, nrow):
                for j in range(1, ncol):
                    if matrix[i][j] != matrix[i-1][j-1]:
                        return False
            return True

