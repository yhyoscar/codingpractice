class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        method = 'bs' # ['bs', 'minheap', 'maxheap']        
        N = len(nums)
        
        # binary search for inserting the new element
        if method == 'bs':
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
        
        # using min-heap
        if method == 'minheap':
            tmp = nums[:k]
            for i in range(k)[::-1]:
                self.heapify_min(tmp, k, i)
            for i in range(k,len(nums)):
                if nums[i] > tmp[0]:
                    tmp[0] = nums[i]
                    self.heapify_min(tmp, k, 0)
            return tmp[0]
        
        # using max-heap
        if method == 'maxheap':            
            for i in range(N)[::-1]:
                self.heapify_max(nums, N, i)
            for i in range(k-1):
                x = nums.pop(0)
                self.heapify_max(nums, N-i-1, 0)
            return nums[0]

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
    def heapify_min(self, array, n, i):
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
            self.heapify_min(array, n, ileft)
            self.heapify_min(array, n, iright)        
        return

    # max heap
    def heapify_max(self, array, n, i):
        if i<n:
            imax   = i
            ileft  = 2*i+1
            iright = 2*i+2
            if ileft < n and array[imax] < array[ileft]:
                imax = ileft
            if iright < n and array[imax] < array[iright]:
                imax = iright
            if imax != i:
                array[imax], array[i] = array[i], array[imax]
            self.heapify_max(array, n, ileft)
            self.heapify_max(array, n, iright)        
        return
    
