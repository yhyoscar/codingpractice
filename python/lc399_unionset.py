
from collections import defaultdict

class Node:
    def __init__(self, key, parent, exchange):
        self.key = key
        self.parent = parent
        self.wt = exchange

#parent = dict{'a':parent of a, 'b':parent of b, ...}
#nchild = dict('d':1, 'a':2, 'b':1, 'c':0, 'e':0)

#b/e

class Solution:        
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        parent = defaultdict(lambda: None)
        wt = defaultdict(lambda: 0.0)        
        for i in range(len(values)):
            if equations[i][0] in list(parent.keys()):
                p, fac = self.findparent(parent, wt, equations[i][0], 1.0 )
                parent[p] = equations[i][1]
                wt[p] = 1.0/values[i]/fac
            else:
                parent[equations[i][0]] = equations[i][1]
                wt[equations[i][0]] = 1.0/values[i]
                
            if equations[i][1] not in parent.keys():
                parent[equations[i][1]] = None
                wt[equations[i][1]] = 1.0
        
        print(dict(parent))
        print(dict(wt))

        out = []
        for q in queries:
            if q[0] not in list(parent.keys()) or q[1] not in list(parent.keys()):
                out.append(-1.0)
            else:
                px, facx = self.findparent(parent, wt, q[0], 1.0)
                py, facy = self.findparent(parent, wt, q[1], 1.0)
                if px == py:
                    out.append(facy/facx)
                else:
                    out.append(-1.0)        
        return  out
    
    def findparent(self, parent, wt, x, fac):
        flag = 2
        if flag == 1:
            if parent[x] is None:
                return x, fac
            else:
                return self.findparent(parent, wt, parent[x], fac*wt[x])                
        if flag == 2:
            fac = 1.0
            current = x
            while parent[current] is not None:
                fac = fac * wt[current]
                current = parent[current]
            return current, fac

s = Solution()
print( s.calcEquation([ ["d", "g"], ["d", "a"], ['d','f'], ['b','a'] ], [6.0, 3.0, 4.0, 1.0], [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]) )



