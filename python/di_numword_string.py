# Given a string with num and words, e.g. "123 34 hdhb kk 2 aa"
# output a new string in which the num and words are in order: "2 34 aa hdhb 123 kk"

def ordernumstr(strin):
    slist = strin.split(' ')
    flag = []
    strs = []
    nums = []
    for s in slist:
        if s.isdigit():
            flag.append(True)
            nums.append(int(s))
        else:
            flag.append(False)
            strs.append(s)
    strout = ''
    strs = sorted(strs)
    nums = sorted(nums)
    for f in flag:
        if f:
            strout += format(nums.pop(0))+' '
        else:
            strout += strs.pop(0) + ' '
    return strout.strip()

ordernumstr('123 34 hdhb kk 2 aa')


