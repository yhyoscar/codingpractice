

def check_repeat(string):
    rchar = ''
    loc = [0, 0]
    replist = []
    for i in range(len(string)):
        if string[i] == rchar:
            loc[1] = i 
        else:
            if loc[1] - loc[0] > 1:
                replist.append([loc[0], loc[1]])
            rchar = string[i]
            loc[0] = i
            loc[1] = i
    if loc[1] > loc[0]:
        replist.append(loc)
    return replist

def powerset_dfs(n):
    if n <= 1:
        return ['0', '1']
    else:
        tmp = powerset_dfs(n-1)
        return [x+'0' for x in tmp] + [x+'1' for x in tmp]

print(powerset_dfs(3))

print(check_repeat('hellloooo'))

