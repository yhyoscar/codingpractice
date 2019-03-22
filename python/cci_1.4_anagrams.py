# Write a method to decide if two strings are anagrams or not.

def check_anagrams(s1, s2):
    if len(s1) == len(s2):
        for i in range(len(s1)):
            if not (s1[i] == s2[-i-1]):
                return False
        return True
    else:
        return False

if __name__ == '__main__':
    s1 = 'abcd'; s2 = 'dcba'; print(s1, s2, check_anagrams(s1,s2))
    s1 = 'abcde'; s2 = 'edcb'; print(s1, s2, check_anagrams(s1,s2))
    s1 = 'abcd'; s2 = 'dcbe'; print(s1, s2, check_anagrams(s1,s2))


