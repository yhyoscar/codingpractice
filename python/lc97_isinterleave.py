# lc 97
class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s3) == len(s1) + len(s2):
            table = [[False for i in range(len(s1)+1)] for j in range(len(s2)+1)]
            table[0][0] = True
            
            for j in range(1, len(s1)+1):
                if table[0][j-1] and s1[j-1] == s3[j-1]: 
                        table[0][j] = True

            for i in range(1, len(s2)+1):
                if table[i-1][0] and s2[i-1] == s3[i-1]: 
                        table[i][0] = True
                for j in range(1, len(s1)+1):
                    if table[i-1][j] and (s2[i-1] == s3[i+j-1]):
                        table[i][j] = True
                    if table[i][j-1] and (s1[j-1] == s3[i+j-1]):
                        table[i][j] = True                    
            #for x in table: print(x)
                        
            return table[-1][-1]
        else:
            return False
        
