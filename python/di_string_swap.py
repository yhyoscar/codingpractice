

def swap(string1, string2):
    if len(string1) != len(string2):
        return 'error 1'
    else:
        if len(string1) < 2:
            return 'error 2'
        else:
            diff = []
            table = {}
            for i in range(len(string1)):
                if string1[i] != string2[i]:
                    table[string1[i]] = string2[i]
                    diff.append(string1[i])
            print(table, diff)            
            e = diff[0]
            for i in range(len(table)):
                print(e, diff)
                if e not in diff: e = diff[0]
                diff.pop(0)
                e = table[e]
            
            if len(diff)==0:
                return len(table)
            else:
                return False

print(swap('conSerVE', 'conVerES'))


