# Binary tree traversal questions like left view, right view, top view, bottom view, maximum of a level, minimum of a level, children sum property, diameter etc.

class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right
        return
    
# construct a binary search tree from an array
def construct_BST(array):
    n = len(array)
    if n > 0:
        root = TreeNode(value=array[0])
        for i in range(1,n):
            node = TreeNode(value=array[i])
            construct_BST_recur(root, node)
    else:
        root = None
    return root

def construct_BST_recur(root, node):
    if root is not None:
        if node.value < root.value:
            if root.left is None:
                root.left = node
            else:
                construct_BST_recur(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                construct_BST_recur(root.right, node)
    return 

def traverse(root, way='inorder'):
    vout = []
    if way == 'inorder':
        traverse_inorder(root, vout)
    if way == 'preorder':
        traverse_preorder(root, vout)
    if way == 'postorder':
        traverse_postorder(root, vout)
    if way == 'levelorder':
        traverse_levelorder(root, vout)
    return vout

# traverse in-order
def traverse_inorder(root, vout):
    if root is not None:
        traverse_inorder(root.left, vout)
        vout.append(root.value)
        traverse_inorder(root.right, vout)
    return

# traverse pre-order
def traverse_preorder(root, vout):
    if root is not None:
        vout.append(root.value)
        traverse_preorder(root.left, vout)
        traverse_preorder(root.right, vout)
    return

# traverse post-order
def traverse_postorder(root, vout):
    if root is not None:
        traverse_postorder(root.left, vout)
        traverse_postorder(root.right, vout)
        vout.append(root.value)
    return

# level order traverse with hash table (same as breadth first search)
def traverse_levelorder_hash(root, htable, depth):
    if root is not None:
        if not (depth in htable): 
            htable[depth] = [root.value]
        else:
            htable[depth].append(root.value)

        htable = traverse_levelorder_hash(root.left, htable, depth+1)
        htable = traverse_levelorder_hash(root.right, htable, depth+1)
    return htable

# vertical order traverse
def traverse_verticalorder_hash(root, htable, dis):
    if root is not None:
        if not (dis in htable):
            htable[dis] = [root.value]
        else:
            htable[dis].append(root.value)
        htable = traverse_verticalorder_hash(root.left, htable, dis-1)
        htable = traverse_verticalorder_hash(root.right, htable, dis+1)
    return htable


# left view
def traverse_left(root, depth, dps, vout):
    if root is not None:
        if not (depth in dps):
            vout.append(root.value)
            dps.append(depth)
        vout = traverse_left(root.left, depth+1, dps, vout)
        vout = traverse_left(root.right, depth+1, dps, vout)
    return vout

# right view
def traverse_right(root, depth, dps, vout):
    if root is not None:
        if not (depth in dps):
            vout.append(root.value)
            dps.append(depth)
        vout = traverse_right(root.right, depth+1, dps, vout)
        vout = traverse_right(root.left, depth+1, dps, vout)
    return vout

# top view
def top_view(root):
    htable = traverse_verticalorder_hash(root, {}, 0)
    view = []
    for i in sorted(htable.keys()):
        view.append(htable[i][0])
    return view

# bottom view
def bottom_view(root):
    htable = traverse_verticalorder_hash(root, {}, 0)
    view = []
    for i in sorted(htable.keys()):
        view.append(htable[i][-1])
    return view

if __name__ == '__main__':
    root = construct_BST([4,2,6,0,3,5,8,7,1])
    print('in-order: ', traverse(root, way='inorder') )
    print('pre-order: ', traverse(root, way='preorder') )
    print('post-order: ', traverse(root, way='postorder') )
    print('left view: ', traverse_left(root, 0, [], []) )
    print('right view: ', traverse_right(root, 0, [], []) )
    print('top view: ', top_view(root) )
    print('bottom view: ', bottom_view(root) )
    print('level order with hash table: ', traverse_levelorder_hash(root, {}, 0))
    print('vertical order with hash table: ', traverse_verticalorder_hash(root, {}, 0))
    
