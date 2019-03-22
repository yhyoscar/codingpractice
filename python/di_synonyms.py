
def is_synonyms(relations, queries):
    table = {}
    for r in relations:
        exist0, parent0 = find_parent(table, r[0])
        exist1, parent1 = find_parent(table, r[1])
        if not exist0:
            if not exist1:
                table[r[0]] = r[1]
                table[r[1]] = None
            else:
                table[r[0]] = parent1
        else:
            if not exist1:
                table[parent0] = r[1]
                table[r[1]] = None
            else:
                table[parent0] = parent1
    flag = []
    for q in queries:
        exist0, parent0 = find_parent(table, q[0])
        exist1, parent1 = find_parent(table, q[1])
        if (not exist0) or (not exist1):
            flag.append(False)
        else:
            if parent0 == parent1:
                flag.append(True)
            else:
                flag.append(False)
    
    return flag

def find_parent(table, x):
    if x not in table:
        return False, None
    else:
        if table[x] is None:
            return True, x
        else:
            return find_parent(table, table[x])
            
print(is_synonyms([('a', 'b'), ('b', 'c'), ('d', 'e')], [('a', 'c'), ('a', 'e'), ('b', 'x')] ))


