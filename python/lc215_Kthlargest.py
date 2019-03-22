class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # using heap
        if False:
            tmp = nums[:k]
            for i in range(k)[::-1]:
                self.heapify(tmp, k, i)
            for i in range(k,len(nums)):
                if nums[i] > tmp[0]:
                    tmp[0] = nums[i]
                    self.heapify(tmp, k, 0)
            return tmp[0]
        
        if True:
            tmp = sorted( nums[:k] )
            for i in range(k, len(nums)):
                if nums[i]>=tmp[-1]:
                    tmp.pop(0)
                    tmp.append(nums[i])
                else:
                    if nums[i]>tmp[0]:
                        j = self.binary_search(tmp, 0, k-1, nums[i])
                        tmp.insert(j+1, nums[i])
                        tmp.pop(0)
            return tmp[0]

    # binary search
    def binary_search(self, array, start, end, x):
        #print(array, start, end, x)
        if (start+1)==end:
            return start
        else:
            mid = (start+end)//2
            if x < array[mid]:
                return self.binary_search(array, start, mid, x)
            else:
                return self.binary_search(array, mid, end, x)
            
            
    # min heap
    def heapify(self, array, n, i):
        if i<n:
            imin   = i
            ileft  = 2*i+1
            iright = 2*i+2
            if ileft < n and array[imin] > array[ileft]:
                imin = ileft
            if iright < n and array[imin] > array[iright]:
                imin = iright
            if imin != i:
                array[imin], array[i] = array[i], array[imin]
            self.heapify(array, n, ileft)
            self.heapify(array, n, iright)        
        return
