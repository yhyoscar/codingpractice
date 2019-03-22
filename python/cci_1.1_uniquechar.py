# Implement an algorithm to determine if a string has all unique characters. 
# What if you can not use additional data structures?

# method 1: use hash table (dictionary)
def check_unique(s):
    d = {}
    for c in s:
        if c in d.keys():
            d[c] += 1
        else:
            d[c] = 1
    if len(d) == sum(d.values()):
        return True
    else:
        return False

# method 2: no additional data structure
def check_unique_m2(s):
    n = len(s)
    for i in range(n):
        for j in range(i):
            if s[i] == s[j]: 
                return False
    return True

if __name__ == '__main__':
    s = 'abcde'
    print(s, check_unique(s), check_unique_m2(s))
    s = 'aabcdee'
    print(s, check_unique(s), check_unique_m2(s))

