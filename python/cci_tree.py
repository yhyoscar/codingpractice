# Given an array, create a binary search tree, and sort the array by traverse it In-Order
# implement in order, pre order, and post order traverse
# note: pre-order is equivelent to DFS (depth-first search)

class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.visit = False
        self.value = value
        self.left = left
        self.right = right
        return

def add_nodes(root, array):
    for i in array:
        node = TreeNode(value=i)
        add_node_recur(root, node)
    return

# bineary search tree
def add_node_recur(root, node):
    if node.value < root.value:
        if root.left is None:
            root.left = node
        else:
            add_node_recur(root.left, node)
    else:
        if root.right is None:
            root.right = node
        else:
            add_node_recur(root.right, node)
    return

def traverse_inorder(root):
    if root is not None:
        traverse_inorder(root.left)
        print(root.value, end=' ')
        traverse_inorder(root.right)
    return

def traverse_preorder(root):
    if root is not None:
        print(root.value, end=' ')
        traverse_preorder(root.left)
        traverse_preorder(root.right)
    return

def traverse_postorder(root):
    if not (root is None):
        traverse_postorder(root.left)
        traverse_postorder(root.right)
        print(root.value, end=' ')
    return


def bfs(root):
    q = [root]
    while len(q) > 0:
        a = q.pop(0)
        print(a.value, end=' ')
        if a.left is not None: q.append(a.left)
        if a.right is not None: q.append(a.right)
        print('[', end='')
        for x in q:
            print(x.value, end=',')
        print(']')
    return

# print zig-zeg layers
def print_layers(root):
    q = [root]
    level = [0]
    pk = 0
    while len(q) > 0:
        if level[0] == level[-1] and pk==level[0]:
            if level[0]%2 == 0:
                print(level[0], [i.value for i in q])
            else:
                print(level[0], [i.value for i in q[::-1]])
            pk += 1
        a = q.pop(0)
        k = level.pop(0)
        #print(a.value, ': level', k)
        if a.left is not None: 
            q.append(a.left)
            level.append(k+1)
        if a.right is not None:
            q.append(a.right)
            level.append(k+1)

    return

def dfs(root):
    q = [root]
    while len(q) > 0:
        a = q.pop()
        print(a.value, end=' ')
        if a.right is not None: q.append(a.right)
        if a.left is not None: q.append(a.left)
        print('[', end='')
        for x in q:
            print(x.value, end=',')
        print(']')
    return

def minvaluenode(root):
    pointer = root
    while pointer.left is not None:
        pointer = pointer.left
    return pointer

def deletenode(root, key):
    if root is None:
        return None
    else:
        if key < root.value:
            root.left = deletenode(root.left, key)
        elif key > root.value:
            root.right = deletenode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:    
                successor = minvaluenode(root.right)
                root.value = successor.value
                root.right = deletenode(root.right, successor.value)
        return root

# get hash table of depth
def depth_table(root, table, depth):
    if root is not None:
        if depth not in table.keys():
            table[depth] = [root.value]
        else:
            table[depth].append(root.value)
        depth_table(root.left, table, depth+1)
        depth_table(root.right, table, depth+1)
    return

# get hash table of horizontal distance
def dis_table(root, table, dis):
    if root is not None:
        if dis not in table.keys():
            table[dis] = [root.value]
        else:
            table[dis].append(root.value)
        dis_table(root.left, table, dis-1)
        dis_table(root.right, table, dis+1)
    return

if __name__ == '__main__':
    #s = [4,5,2,1,6,7,3]
    import numpy as np
    
    n = 20
    #s = np.random.choice(list(range(1,n+1)), size=n, replace=False)
    s = [13,4,9,8,18,3,6,19,12,15,10,7,11,1,16,17,5,2,14,20]
    #s = [5,7,20,14,8,4,15,3,2,19,9,13,10,16,11,1,18,12,6,17]
    print('---------------------------------------------------------')
    for i in s:   print(i, end=',')
    print('\n---------------------------------------------------------')
    root = TreeNode(value=s[0])
    add_nodes(root, s[1:])

    print('in order:'); traverse_inorder(root); print('')
    print('pre order:'); traverse_preorder(root); print('')
    print('post order:'); traverse_postorder(root); print('')
    print('DFS: '); dfs(root); print('')
    print('BFS: '); bfs(root); print('')
    print('print layers:'), print_layers(root)
    table = {}; depth_table(root, table, 0); print('depth table: ', table)
    table = {}; dis_table(root, table, 0); print('distance table: ', table)
    print('delete node: '); root = deletenode(root, 13); bfs(root)

