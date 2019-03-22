# Assume you have a method isSubstring which checks if one word is 
# a substring of another. Given two strings, s1 and s2, write code 
# to check if s2 is a rotation of s1 using only one call to isSubstring 
# (i.e., “waterbottle” is a rotation of “erbottlewat”).
 
def issubstring(s1, s2):
    if s1 in s2:    return True
    else:   return False

def isrotation(s1, s2):
    if len(s1) == len(s2):
        if issubstring(s1, s2+s2): return True
        else:   return False
    else:
        return False

if __name__ == '__main__':
    s1 = 'apple'; s2 = 'pleap'; print(s1, s2, isrotation(s1, s2))
    s1 = 'apple'; s2 = 'ppale'; print(s1, s2, isrotation(s1, s2))



