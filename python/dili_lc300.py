class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 1:
            return len(nums)
        else:
            s = [1 for x in nums]
            for i in range(1, len(nums)):
                #print(s)
                #s[i] = s[i-1]
                
                for j in range(i):
                    if s[i] < s[j]+1 and nums[j] < nums[i]:
                        s[i] = s[j] + 1
            return max(s)
            
