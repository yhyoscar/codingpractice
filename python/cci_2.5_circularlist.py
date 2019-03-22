# Given a circular linked list, implement an algorithm which returns node at the beginning of the loop.
# DEFINITION
# Circular linked list: A (corrupt) linked list in which a node’s next pointer points to an earlier node, 
# so as to make a loop in the linked list.
# EXAMPLE
# input: A -> B -> C -> D -> E -> C [the same C as earlier]
# output: C

# 1. create a hash table of occuring times
# 2. loop from end to first to get the first element in cycle
def circular_element(s):
    ht = {}
    for e in s:
        if e in ht:
            ht[e] += 1
        else:
            ht[e] = 0
    n = ht[s[-1]]
    ce = s[-1]
    for e in s[::-1]:
        if ht[e] < n:
            break
        else:
            ce = e
    return ce

if __name__ == '__main__':
    s = list('abcdefgcde')
    print(s,':',circular_element(s))


