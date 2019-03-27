#lc149

# Definition for a point.
# class Point:
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

class Solution:
    def maxPoints(self, points: List[Point]) -> int:
        if len(points) < 2:
            return len(points)
        else:
            from collections import defaultdict
            nmax = 1
            table = defaultdict(set)
            for i in range(1,len(points)):
                for j in range(i):
                    out = self.slope_inter(points[i], points[j])
                    table[out].add(i)
                    table[out].add(j)
                    nmax = max(nmax, len(table[out]))
            return nmax
    
    def slope_inter(self, p1, p2):
        import math
        if p1.x == p2.x:
            return 0, 0, p1.x, 1
        else:
            # use two integers to represent slope
            s1 = int(p2.y-p1.y)
            s2 = int(p2.x-p1.x)
            ds = math.gcd(s1, s2)
            if s1*s2>=0:
                s1 = abs(s1); s2 = abs(s2)
            else:
                s1 = -abs(s1); s2 = abs(s2)
            
            # use two integers to represent intersection
            i1 = int(p1.y*(p2.x-p1.x) - p1.x*(p2.y-p1.y))
            i2 = int(p2.x-p1.x)
            di = math.gcd(i1, i2)                
            if i1*i2 >= 0:
                i1 = abs(i1); i2 = abs(i2)
            else:
                i1 = -abs(i1); i2 = abs(i2)

            return int(s1/ds), int(s2/ds), int(i1/di), int(i2/di)

