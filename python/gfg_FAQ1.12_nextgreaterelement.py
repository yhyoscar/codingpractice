# Given an array, print the Next Greater Element (NGE) for every element. The Next greater Element for an element x is the first greater element on the right side of x in array. Elements for which no greater element exist, consider next greater element as -1.


# loop from right to left
# use a stack restore the great elements 
# pop out the smaller elements

def NGE(array):
    n = len(array)
    s = [-1 for i in range(n)]
    stack = [array[n-1]]
    for i in range(n-1)[::-1]:
        while (len(stack)>0) and (stack[-1] <= array[i]):
            stack.pop()

        if len(stack) == 0:
            s[i] = -1
        else:
            s[i] = stack[-1]

        stack.append(array[i])
    return s

print( NGE([4,5,2,25]) )
print( NGE([13,7,6,12]) )
        


