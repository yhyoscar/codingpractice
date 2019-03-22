# 239

import numpy as np

class Solution:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        def heapify(array, ids, n, i):
            if i<n:
                imax = i
                ileft = imax*2 + 1
                iright = imax*2 + 2
                if ileft<n and array[imax] < array[ileft]:
                    imax = ileft
                if iright<n and array[imax] < array[iright]:
                    imax = iright
                if imax != i:
                    array[imax], array[i] = array[i], array[imax]
                    ids[imax], ids[i] = ids[i], ids[imax]
                    heapify(array, ids, n, imax)
            
                    
        def decreasekey(array, ids, i):
            if i>0:
                iparent = (i-1)//2
                if iparent >= 0 and array[iparent] < array[i]:
                    array[iparent], array[i] = array[i], array[iparent]
                    ids[iparent], ids[i] = ids[i], ids[iparent]
                    decreasekey(array, ids, iparent)
            return
        
        if len(nums)>0:
            if k==1:
                return nums                
            else:
                if True:
                    q = []
                    maxlist = []
                    for i in range(k):
                        print(i, 'before: ', np.array(nums)[q], maxlist)                        
                        while q and nums[i] >= nums[q[-1]]:
                            q.pop()
                        q.append(i)                    
                        print(i, 'after', np.array(nums)[q], maxlist)
                        
                    for i in range(k,len(nums)):
                        maxlist.append(nums[q[0]]) 
                        print(i, 'before: ', np.array(nums)[q], maxlist)
                        while q and q[0]<=i-k:
                            q.pop(0)
                        print(i, 'mid: ', np.array(nums)[q], maxlist)
                        while q and nums[i] >= nums[q[-1]]:
                            q.pop()
                        q.append(i)
                        print(i, 'after: ', np.array(nums)[q], maxlist)                        
                        
                    maxlist.append(nums[q[0]])
                    return maxlist
                
                if False:
                    tmp = [x for x in nums[0:k]]
                    ids = list(range(k))
                    for i in range(k)[::-1]:
                        heapify(tmp, ids, k, i)
                    maxlist = [tmp[0]]
                    for i in range(len(nums)-k):
                        i0 = ids.index(i)
                        # delete the first element
                        tmp[i0] = float('Inf')
                        decreasekey(tmp, ids, i0)
                        # replace with i+k element
                        tmp[0] = nums[i+k]
                        ids[0] = i+k
                        heapify(tmp, ids, k, 0)
                        maxlist.append(tmp[0])
                    return maxlist

                    
                if False:
                    tmp = nums[0:k]
                    maxlist = [max(tmp)]
                    for i in range(k,len(nums)):
                        if nums[i] > maxlist[-1]:
                            nextmax = nums[i]
                        else:
                            if maxlist[-1] == tmp[0]:
                                nextmax = max(nums[i], max(tmp[1:]))
                            else:    
                                nextmax = maxlist[-1]
                        maxlist.append(nextmax)
                        tmp.pop(0)
                        tmp.append(nums[i])
                    return maxlist
        else:
            return []
        

class Solution2:
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        if len(nums)>0:
            if k==1:
                return nums                
            else:
                tmp = nums[0:k]
                maxlist = [max(tmp)]
                for i in range(k,len(nums)):
                    if nums[i] > maxlist[-1]:
                        nextmax = nums[i]
                    else:
                        if maxlist[-1] == tmp[0]:
                            nextmax = max(nums[i], max(tmp[1:]))
                        else:    
                            nextmax = maxlist[-1]
                    maxlist.append(nextmax)
                    tmp.pop(0)
                    tmp.append(nums[i])
                return maxlist
        else:
            return []

s = Solution()
s.maxSlidingWindow([1,3,-1,-3,-2,3,6,7], 3)

