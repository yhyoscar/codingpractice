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

def find_path(root, target):
    if root is not None:
        if root.value == target:
            return [root.value]
        else:
            path_left = find_path(root.left, target)
            path_right = find_path(root.right, target)
            if path_left is not None:
                return [root.value] + path_left
            if path_right is not None:
                return [root.value] + path_right

# lowest common ancestor
def lca(root, target1, target2):
    path1 = find_path(root, target1)
    path2 = find_path(root, target2)
    for i in range(min(len(path1), len(path2))):
        if path1[i] == path2[i]:
            a = path1[i]
    return a

# find the LCA with only one traversal
# return: flag of existance of target1, flag of target2, LCA node
def lca_onetrav(root, target1, target2):
    if root is None: 
        return False, None
    else:
        if root.value == target1 or root.value == target2:
            return True, None
        
        lflag, lvalue = lca_onetrav(root.left, target1, target2)
        rflag, rvalue = lca_onetrav(root.right, target1, target2)
        
        print(root.value, lflag, lvalue, rflag, rvalue)
        if lflag and rflag:
            return True, root.value
        else:
            if lvalue is not None:
                return True, lvalue
            if rvalue is not None:
                return True, rvalue
            return lflag or rflag, None


if __name__ == '__main__':
    root = construct_BST([4,2,6,0,3,5,8,7,1,-1])
    print(find_path(root, 8)) 
    print(lca(root, 5, 7))
    print( lca_onetrav(root, 1, -1) )
    #print(node.value)
    

