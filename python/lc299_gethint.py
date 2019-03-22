class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        n = len(secret)
        ht_s = {format(i):0 for i in range(10)}
        ht_g = {format(i):0 for i in range(10)}
        
        a = 0
        for i in range(n):
            ht_s[secret[i]] += 1
            ht_g[guess[i]] += 1
            if secret[i] == guess[i]:
                a += 1
        
        b = 0
        for i in range(10):
            b += min(ht_s[format(i)], ht_g[format(i)])
        b -= a
        
        return format(a)+'A'+format(b)+'B'
        

