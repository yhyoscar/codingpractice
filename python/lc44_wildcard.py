class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if len(p) == 0:
            if len(s) == 0: return True
            else: return False
        else:
            if len(s) == 0:
                if ''.join(set(p)) == '*': return True
                else: return False
            else:
                flag = [[False for y in s] for x in p]                
                minlen = [0]    # minimum required length of string s
                for x in p:
                    if x == '*': minlen.append(minlen[-1])
                    else: minlen.append(minlen[-1] + 1)
                minlen.pop(0)
                
                # first row
                if p[0] == '*':  
                    flag[0] = [True for y in s]
                else: 
                    if (s[0] == p[0]) or (p[0] == '?'): flag[0][0] = True                    
                    
                for i in range(1, len(p)):
                    # first column
                    if (p[i] in ['*', '?', s[0]]) and flag[i-1][0] and (minlen[i] <= 1): flag[i][0] = True
                    for j in range(1, len(s)):
                        if ('a'<=p[i]<='z' and flag[i-1][j-1] and (p[i] == s[j])) or \
                            (p[i] == '?' and flag[i-1][j-1]) or \
                            (p[i] == '*' and (flag[i-1][j-1] or flag[i-1][j] or flag[i][j-1])):
                            flag[i][j] = True

                return flag[-1][-1]
                            
                        
