"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if root is not None:
            # traverse the tree with BFS method
            q = [root]  # queue of nodes
            k = [0]     # depth of nodes
            level = 0   
            while len(q) > 0:
                if len(k) > 0:
                    if (k[0] == k[-1]) and (k[0] == level):
                        # all nodes are on the same level/depth
                        for i in range(len(q)-1): 
                            q[-1].next = None
                        level += 1
                current = q.pop(0)  # current node
                ck = k.pop(0)       # depth of current node
                if current.left is not None:
                    q.append(current.left)
                    k.append(ck+1)
                if current.right is not None:
                    q.append(current.right)
                    k.append(ck+1)
            return root
    

