# 283
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        n = len(nums)
        while i<n and j<n:
            if nums[i]!=0: i+=1
            if nums[j]==0: j+=1
            if i<n and j<n and nums[i]==0 and nums[j]!=0 and i<j: 
                nums[i],nums[j] = nums[j],nums[i]
                i+=1
                j+=1
            if i>=j:
                j = i
        return
