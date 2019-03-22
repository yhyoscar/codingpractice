class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        table = {}
        flag = True
        for i in range(len(s)):
            if s[i] in table.keys():
                if t[i] != table[s[i]]: return False
            else:
                if t[i] in table.values(): return False
                else: table[s[i]] = t[i]
        return flag
