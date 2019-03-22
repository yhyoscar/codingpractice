# Implement an algorithm to delete a node in the middle of a single linked list, given only access to that node.
# EXAMPLE
# Input: the node ‘c’ from the linked list a->b->c->d->e
# Result: nothing is returned, but the new linked list looks like a->b->d->e

def deletenode(slist, node):
    # loop of list:
    #       if node == element: remove it from the list and return
    #       else: next element
    n = len(slist)
    for i in range(n):
        if slist[i] == node:
            slist.pop(i)
            return
    return 

if __name__ == '__main__':
    s = ['a', 'bc', 2, 4]
    print(s)
    deletenode(s, 'a')
    print(s)
    deletenode(s, 2)
    print(s)
    deletenode(s, 1)
    print(s)

