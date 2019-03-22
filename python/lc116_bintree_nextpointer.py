# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

def build_tree_bfs(root, array):
    root.val = array[0]
    q = [root]
    i = 1
    while len(q) > 0:
        cnode = q.pop(0)
        if i<len(array):
            cnode.left = TreeLinkNode(array[i])
            q.append(cnode.left)
            i += 1
        if i<len(array):
            cnode.right = TreeLinkNode(array[i])
            q.append(cnode.right)
            i += 1
    return root

def print_tree_bfs(root):
    q = [root]
    while len(q) > 0:
        cnode = q.pop(0)
        if cnode.next is None:
            print( [cnode.val, None], end=', ' )
        else:
            print( [cnode.val, cnode.next.val], end=', ')
        if cnode.left is not None:
            q.append(cnode.left)
        if cnode.right is not None:
            q.append(cnode.right)
    print('')
    return

def connect(root):
    q = [root]
    k = [0]
    count = 0
    while len(q) > 0:
        if len(k) > 0:
            if (k[0] == k[-1]) and (k[0] == count):
                for i in range(len(q)-1):
                    q[i].next = q[i+1]
                q[len(q)-1].next = None
                count += 1
        current = q.pop(0)
        ck = k.pop(0)
        if current.left is not None:
            q.append(current.left)
            k.append(ck+1)
        if current.right is not None:
            q.append(current.right)
            k.append(ck+1)
    return 

root = build_tree_bfs( TreeLinkNode(), [0,1,2,3,4,5,6,7,8,9] )
print('before: ')
print_tree_bfs(root)

connect(root)
print('after: ')
print_tree_bfs(root)


