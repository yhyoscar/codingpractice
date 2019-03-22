class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        kmax = 2; ntime = len(prices)
        S = [[0 for i in range(ntime+1)] for k in range(kmax+1)]
        
        for k in range(1, kmax+1):
            for i in range(2, ntime+1):
                S[k][i] = max(S[k][i-1], max([prices[i-1]-prices[j-1]+S[k-1][j-1]  for j in range(1,i)]))
    
        return S[-1][-1]
        
        

