# find duplicates in O(n) time and O(1) extra space

def find_duplicate(nums):
    if True:
        zeros = 0
        for x in nums:
            if x == 0: zeros += 1
            if nums[abs(x)] > 0:
                nums[abs(x)] *= -1
            elif nums[abs(x)] < 0:
                print(abs(x))
        if nums[0] == 0:
            if zeros == 2: print(0)
        
    if False:
        count = [0]*len(nums)
        for x in nums:
            count[x] += 1
            if count[x] == 2:
                print(x)
    return

find_duplicate([4, 2, 3, 1, 3, 6, 6, 0, 1, 0])


