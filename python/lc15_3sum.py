class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        for i in range(len(nums)-1, 1, -1):
            for j in range(i-1, 0, -1):
                if -(nums[i]+nums[j]) in nums and nums.index(-(nums[i]+nums[j])) < j:
                    tmp = sorted([nums[i],nums[j],-(nums[i]+nums[j])])
                    s.add( ' '.join([format(x) for x in tmp]) ) 

        return [[int(i) for i in x.split(' ')] for x in s]
