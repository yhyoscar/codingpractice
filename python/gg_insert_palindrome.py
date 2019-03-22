

def mininsert(string):
    if len(string) <= 1: 
        return 0
    else:
        if string[0] == string[-1]:
            return mininsert(string[1:-1])
        else:
            return min(mininsert(string[1:]), mininsert(string[:-1])) + 1


print(mininsert('abcde'))


