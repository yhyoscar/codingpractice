#Given a list of zeros and ones, find the index of the last zero
#i.e. [0,0,0,1,1,1,1] return 2
# hint: binary search O(log(n))

def lastindex(array, istart, iend):
    if istart > iend:
        return None
    else:
        if istart == iend:
            if array[istart] == 0: return istart
            else: return None
        else:
            imid = (istart+iend)//2
            ileft  = lastindex(array, istart, imid)
            iright = lastindex(array, imid+1, iend)
            if ileft is None:
                if iright is None:
                    return None
                else:
                    return iright
            else:
                if iright is None:
                    return ileft
                else:
                    return max(ileft, iright)

print(lastindex([1,0,1,0,0,1,1], 0, 6))
