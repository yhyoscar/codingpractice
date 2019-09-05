class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.left = []
        self.right = []
    
    def heapify_bottomup(self, array, i, flag='min'):
        if i > 0:
            iparent = int((i-1)//2)
            im = i
            if flag == 'min':
                if array[iparent] > array[i]: im = iparent
            if flag == 'max':
                if array[iparent] < array[i]: im = iparent
            if i != im:
                array[im], array[i] = array[i], array[im]
                self.heapify_bottomup(array, iparent, flag=flag)
    
    
    def heapify(self, array, i, flag='min'):
        if i < len(array)-1:
            ileft = 2*i + 1
            iright = 2*i + 2
            im = i
            if ileft < len(array):
                if flag == 'min':        
                    if array[ileft] < array[im]:
                        im = ileft
                if flag == 'max':        
                    if array[ileft] > array[im]:
                        im = ileft
            if iright < len(array):
                if flag == 'min':        
                    if array[iright] < array[im]:
                        im = iright
                if flag == 'max':        
                    if array[iright] > array[im]:
                        im = iright
            if im != i:
                array[i], array[im] = array[im], array[i]            
                self.heapify(array, im, flag=flag)
    
    
    def heap_delete(self, array, flag='min'):
        array[0], array[-1] = array[-1], array[0]
        array.pop()
        self.heapify(array, 0, flag=flag)
        
        
    def heap_insert(self, array, new, flag='min'):
        array.append(new)
        self.heapify_bottomup(array, len(array)-1, flag=flag)
    

    def addNum(self, num: int) -> None:
        if len(self.left) == len(self.right):
            if len(self.left) > 0:
                if num <= self.right[0]:
                    self.heap_insert(self.left, num, flag='max')
                else:
                    self.heap_insert(self.right, num, flag='min')
            else:
                self.left.append(num)
        
        elif len(self.left) > len(self.right):
            if num >= self.left[0]:
                self.heap_insert(self.right, num, flag='min')
            else:
                self.heap_insert(self.left, num, flag='max')
                self.heap_insert(self.right, self.left[0], flag='min')
                self.heap_delete(self.left, flag='max')
        else:
            if num <= self.right[0]:
                self.heap_insert(self.left, num, flag='max')
            else:
                self.heap_insert(self.right, num, flag='min')
                self.heap_insert(self.left, self.right[0], flag='max')
                self.heap_delete(self.right, flag='min')
        
        #print(self.left, self.right)
        

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            if len(self.left) > 0:
                return (self.left[0] + self.right[0])/2
            else:
                return None
        elif len(self.left) > len(self.right):
            return self.left[0]
        else:
            return self.right[0]
        

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
