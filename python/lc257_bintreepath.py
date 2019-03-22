# lc257
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        allpath = []
        if root is not None: 
            path = ""
            self.recur(root, allpath, path)
        #if len(allpath) > 0:
        #    for x in allpath:
        #        print(x)
        return allpath
    def recur(self, root, allpath, path):
        if root is not None:
            if len(path) > 0:
                path += "->"
            path += format(root.val)
            if root.left is not None: self.recur(root.left, allpath, path)
            if root.right is not None: self.recur(root.right, allpath, path)
            if (root.left is None) and (root.right is None):
                allpath.append(path)
        return
    

