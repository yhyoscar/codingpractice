
def remove_duplicate(string):
    if string is None: return None
    if len(string) < 2: return string
    slist = list(string)

    exist = [False for i in range(256)]
    exist[ord(string[0])] = True
    for i in range(1, len(string)):
        if exist[ord(string[i])]:
            slist[i] = ''
        else:
            exist[ord(string[i])] = True
    return ''.join(slist)


if __name__ == '__main__':
    string = 'aaabbbb'
    print( remove_duplicate(string) )


