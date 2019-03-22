# reverse the digits of an integer

class Solution(object):
    def reverse(self, x):
        if abs(x) < 10: return x
        else:
            sx = str(x)
            if sx[0] == '-': y = -int(sx[1:][::-1])
            else: y = int(sx[::-1])
        return y

print(Solution().reverse(2))
print(Solution().reverse(10))
print(Solution().reverse(-120))
print(Solution().reverse(-0))
print(Solution().reverse(-10))


