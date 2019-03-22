# Design an algorithm and write code to remove the duplicate characters 
# in a string without using any additional buffer. 
# NOTE: One or two additional variables are fine. An extra copy of the array is not.
# FOLLOW UP
# Write the test cases for this method.

def remove_duplicate(s):
    s = list(s)
    n = len(s)
    for i in range(n):
        if s[i] in s[0:i]:
            s[i] = ''
    return ''.join(s)
        
if __name__ == '__main__':
    s = 'aabccbbdef'
    print(s, remove_duplicate(s))

