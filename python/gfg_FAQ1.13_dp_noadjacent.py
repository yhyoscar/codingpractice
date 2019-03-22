# Maximum sum such that no two elements are adjacent
# Given an array of positive numbers, find the maximum sum of a subsequence with the constraint that no 2 numbers in the sequence should be adjacent in the array. So 3 2 7 10 should return 13 (sum of 3 and 10) or 3 2 5 10 7 should return 15 (sum of 3, 5 and 7).Answer the question in most efficient way.


# recursive relation: 
# if flag(n-1) is True: s(n) = max(s(n-1), s(n-2)+a(n)); if s(n-1), flag(n)=False, else flag(n)=True
# else: s(n) = s(n-1)+a(n), flag(n)=True
def maxsum_noadj(array):
    n = len(array)
    flag = [False for i in range(n)]
    s = [0 for i in range(n+1)]
    flag[0] = True
    s[1] = array[0]
    
    for i in range(1,n):
        if flag[i-1]:
            if s[i] > s[i-1]+array[i]:
                flag[i] = False
                s[i+1] = s[i]
            else:
                flag[i] = True
                s[i+1] = s[i-1] + array[i]
        else:
            flag[i] = True
            s[i+1] = s[i] + array[i]
    return s[-1]

print(maxsum_noadj([5, 5, 10, 100, 10, 5]))
print(maxsum_noadj([1,2,3]))
print(maxsum_noadj([1,20,3]))
print(maxsum_noadj([3,2,7,10]))
print(maxsum_noadj([3,2,5,10,7]))

    



