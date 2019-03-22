# 42
class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        rain = 0
        if n > 0:
            mleft = [0 for i in range(n)]
            mleft[0] = height[0]
            for i in range(1, n):
                mleft[i] = max(mleft[i-1], height[i])

            mright = [0 for i in range(n)]
            mright[n-1] = height[n-1]
            for i in range(n-2, -1, -1):
                mright[i] = max(mright[i+1], height[i])

            for i in range(n):
                rain += min(mleft[i], mright[i]) - height[i]
        
        return rain
