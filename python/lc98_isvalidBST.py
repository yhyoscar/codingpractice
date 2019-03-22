# lc 98

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None: 
            return True
        else:
            flag, mintree, maxtree = self.rec(root)
            return flag
        
    def rec(self, root):
        if root is None:
            return None, 0, 0
        else:
            flagleft, minleft, maxleft = self.rec(root.left)
            flagright, minright, maxright = self.rec(root.right)

            if flagleft is None:
                if flagright is None:
                    return True, root.val, root.val
                else:
                    if flagright and (root.val < minright):
                        return True, root.val, maxright
                    else:
                        return False, 0, 0
            else:
                if flagright is None:
                    if flagleft and (root.val > maxleft):
                        return True, minleft, root.val
                    else:
                        return False, 0, 0
                else:
                    if flagleft and flagright and (root.val > maxleft) and (root.val < minright):
                        return True, minleft, maxright
                    else:
                        return False, 0, 0
        
