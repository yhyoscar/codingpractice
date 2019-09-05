# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, x: int) -> bool:
        if root is None:
            return False
        else:
            return self.recur(root, root.val, x)
    
    def recur(self, root, s, target):
        if root.left is None:
            if root.right is None:
                if s == target:
                    return True
                else:
                    return False
            else:
                return self.recur(root.right, s+root.right.val, target)
        else:
            if root.right is None:
                return self.recur(root.left, s+root.left.val, target)
            else:
                return self.recur(root.left, s+root.left.val, target) or self.recur(root.right, s+root.right.val, target)

            
            
