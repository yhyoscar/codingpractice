# Given a sorted (increasing order) array, write an algorithm to create a binary tree with minimal height.

from cci_tree import TreeNode

# recursively insert: middle element as root, left array as left subtree, and right array as right subtree
def minheight(array):
    if len(array) <= 0:
        return None
    else:
        if len(array) == 1:
            return TreeNode(value = array[0])
        else:
            imid = len(array)//2
            node = TreeNode(value = array[imid])
            node.left  = minheight(array[0:imid])
            node.right = minheight(array[imid+1:])
            return node

if __name__ == '__main__':
    root = minheight([1,2,3,4,5,6,7])
    root.traverse_inorder()


