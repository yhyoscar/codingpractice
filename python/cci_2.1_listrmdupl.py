# Write code to remove duplicates from an unsorted linked list.
# FOLLOW UP
# How would you solve this problem if a temporary buffer is not allowed?

# Method 1: use temporary buffer which restore checked elements
def remove_dup(s):
    tmp = []
    for e in s:  
        if not (e in tmp):  tmp.append(e)
    return tmp

# Method 2: no temporary buffer
def remove_dup_nobuf(s):
    # do loop: 
    #       if end, return, 
    #       else check duplicate;
    #           if dup: remove this one
    #           else: next
    n = len(s)
    i = 0
    while True:
        if i+1 > len(s):
            return s
        else:
            if s[i] in s[0:i]:
                s.pop(i)
            else:
                i += 1
    return s


if __name__ == '__main__':
    s = list('aabbbcd')
    print(s, '->', remove_dup(s) )
    s2 = list('aabbbcd')
    print(s2, '->', end=' ')
    print(remove_dup_nobuf(s2))


