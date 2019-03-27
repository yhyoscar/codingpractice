# lc 387
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s)>0:
            h = {}; clist = []
            for x in s:
                if x in h: h[x]+=1
                else: h[x] = 1; clist.append(x)
            n = 999
            cmin = ''
            #print(h)
            for x in clist:
                if h[x] < n: n=h[x]; cmin = x
            if n > 1:
                return -1
            else:
                return list(s).index(cmin)
        else:
            return -1

class Solution:
    def firstUniqChar(self, s: str) -> int:
        method = 3
        
        if method == 1:
            from collections import defaultdict        
            d = defaultdict(int, {})
            for x in s: 
                d[x] += 1
            i = 0
            for x in s:
                if d[x] == 1: return i
                i += 1
            return -1
        
        if method == 2:
            from collections import defaultdict        
            d = defaultdict(list, {})
            for i in range(len(s)): 
                d[s[i]].append(i)
            
            for x in d.keys():
                if len(d[x]) == 1: return d[x][0]
            return -1
        
        if method == 3:
            from collections import defaultdict, OrderedDict      
            d = OrderedDict()
            c = defaultdict(int, {})
            for i in range(len(s))[::-1]:
                d[s[i]] = i
                c[s[i]] += 1
            
            for x in list(d.keys())[::-1]:
                if c[x] == 1: return d[x]
            return -1
        
        

