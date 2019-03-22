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
        
