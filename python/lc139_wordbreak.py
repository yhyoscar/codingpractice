class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ns = len(s)
        nd = len(wordDict)
        method = 'recur'
        
        if method=='bottom-up':
            array = [True] + [False for i in range(ns)]
            for i in range(1, ns+1):
                for j in range(nd):
                    w = wordDict[j]
                    if i-len(w)>=0 and array[i-len(w)] and s[i-len(w):i] == w:
                        array[i] = True
                        break
            return array[-1]
        
        if method == 'recur':
            # (solution, visited)
            array = [[True, True]] + [[False, False] for i in range(ns)]
            return self.recur(array, s, wordDict, ns)
            
    def recur(self, array, s, d, n):            
        if n < 0: return False
        elif n==0: return True
        else:
            if array[n][1]: 
                return array[n][0]
            else:
                for i in range(len(d)):
                    if s[n-len(d[i]):n] == d[i]:
                        array[n][0] = array[n][0] or self.recur(array, s, d, n-len(d[i]))
                array[n][1] = True
                return array[n][0]
            
