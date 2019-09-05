class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        else:
            sublen = [1 for x in s]
            for i in range(1,len(s)):
                for j in range(i-1, i-1-sublen[i-1], -1):
                    if s[i] != s[j]:
                        sublen[i] += 1
                    else:
                        break
            return max(sublen)
