class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        K = 2; ntime = len(prices)
        if ntime <= 1:
            return 0
        else:
            S = [[0 for i in range(ntime)] for k in range(K+1)]
            for k in range(1, K+1):
                mindiff = prices[0]
                for i in range(1, ntime):
                    mindiff = min(mindiff, prices[i]-S[k-1][i-1])
                    S[k][i] = max(S[k][i-1], prices[i]-mindiff)

            return S[-1][-1]
