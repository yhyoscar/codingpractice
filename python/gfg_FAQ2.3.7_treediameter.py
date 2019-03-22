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

# calculate height for a tree
def cal_height(root):
    if root is None:
        return 0
    else:
        if root.left is None and root.right is None:
            return 1
        else:
            return cal_height(root.left) + 1
            return cal_height(root.right) + 1

# calculate diameter of a tree
# D = max(Dleft, Dright, Hleft+Hright+1)
def diameter(root):
    if root is None:
        return 0, 0
    else:
        if root.left is None and root.right is None:
            return 1, 1
        else:
            leftdh = diameter(root.left)
            rightdh = diameter(root.right)
            return max([leftdh[0], rightdh[0], leftdh[1]+rightdh[1]+1]), max([leftdh[1], rightdh[1]]) + 1

if __name__ == '__main__':
    root = construct_BST([4,2,6,0,3,5,8,7,1])
    print( cal_height(root) )
    print( diameter(root.left) )


