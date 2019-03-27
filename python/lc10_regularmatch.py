class Solution:
    def isMatch(self, s: 'str', p: 'str') -> 'bool':
        if len(p) == 0:
            if len(s) == 0: return True
            else: return False
        else:
            if len(s) == 0:
                # if all the even locations are *, return True
                if (''.join(set(p[1::2])) == '*') and p[-1]=='*': return True
                else: return False
            else:
                np = len(p); ns = len(s)
                flag = [[False for j in range(ns+1)] for i in range(np+1)]
                
                # first row: p=''
                flag[0][0] = True   # s='', p=''
                flag[0][1:] = [False for j in range(ns)]    # s='xxx', p=''

                # first column: s=''
                for i in range(1, np+1):
                    if i%2==0 and p[i-1]=='*': 
                        flag[i][0] = flag[i-2][0]
                
                for j in range(1, ns+1):
                    for i in range(1, np+1):
                        if (p[i-1]=='*') and ( (flag[i][j-1] and (p[i-2] in [s[j-1], '.'])) or flag[i-2][j] ):
                                flag[i][j] = True

                        if (p[i-1] in ['.', s[j-1]]) and flag[i-1][j-1]:
                            flag[i][j] = True
                                    
                return flag[-1][-1]
                        
