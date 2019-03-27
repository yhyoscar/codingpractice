class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        else:
            method = 'optim'  # ['simple', 'optim']
            
            if method == 'simple':
                s = [1 for x in nums]
                for i in range(1, len(nums)):
                    for j in range(i):
                        if s[i] < s[j]+1 and nums[j] < nums[i]:
                            s[i] = s[j] + 1

                return max(s)
            
            if method == 'optim':
                # monotonic sequence
                seq = [nums[0]]
                for x in nums[1:]:
                    i = self.binary_search(seq, 0, len(seq), x) 
                    if x > seq[-1]: 
                        seq.append(x)
                    else:
                        seq[i] = x
                return len(seq)

    def binary_search(self, array, start, end, x):
        if start >= end:
            return int(start)
        else:
            mid = int( (start + end)/2 )
            if array[mid] < x:
                return self.binary_search(array, mid+1, end, x)
            else:
                return self.binary_search(array, start, mid, x)
                
