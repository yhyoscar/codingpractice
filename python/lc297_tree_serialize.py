# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None
        return
    
def build_tree_bfs(root, array):
    root.val = array[0]
    q = [root]
    i = 1
    while len(q) > 0:
        cnode = q.pop(0)
        if i<len(array):
            cnode.left = TreeNode(array[i])
            q.append(cnode.left)
            i += 1
        if i<len(array):
            cnode.right = TreeNode(array[i])
            q.append(cnode.right)
            i += 1
    return root

def print_tree_bfs(root):
    q = [root]
    while len(q) > 0:
        cnode = q.pop(0)
        #if cnode.next is None:
        print( cnode.val, end=', ' )
        #else:
        #    print( [cnode.val, cnode.next.val], end=', ')
        if cnode.left is not None:
            q.append(cnode.left)
        if cnode.right is not None:
            q.append(cnode.right)
    print('')
    return

def print_series(s):
    for x in s:
        print(x, end=', ')
    print('')
    return

class Codec:

    def serialize(self, root, flag=1):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        # flag = 2 # 1: pre-order; 2: use stack ; 3: BFS
        if flag == 1:
            if root is None:
                return [None]
            else:
                tmp = [root.val]
                tmp += self.serialize(root.left)
                tmp += self.serialize(root.right)
                return tmp
        if flag == 2:
            stack = [root]
            branch = [0]
            if root is None:
                tmp = []
            else:
                tmp = [root.val]
            if root is not None:
                while len(stack) > 0:
                    if branch[-1] < 2:
                        if branch[-1]==0: 
                            if stack[-1].left is None:
                                tmp.append(None)
                                branch[-1] += 1
                            else:
                                tmp.append(stack[-1].left.val)
                                branch[-1] += 1
                                stack.append(stack[-1].left)
                                branch.append(0)
                        if branch[-1]==1: 
                            if stack[-1].right is None:
                                tmp.append(None)
                                branch[-1] += 1
                            else:
                                tmp.append(stack[-1].right.val)
                                branch[-1] += 1
                                stack.append(stack[-1].right)
                                branch.append(0)
                    else:
                        stack.pop()
                        branch.pop()
            return tmp

        if flag == 3:
            if root is None:
                return []
            else:
                queue = [root]
                tmp = [root.val]
                while len(queue) > 0:
                    node = queue.pop(0)
                    if node is not None:
                        if node.left is None:
                            tmp.append(None)
                            queue.append(None)
                        else:
                            tmp.append(node.left.val)
                            queue.append(node.left)
                        if node.right is None:
                            tmp.append(None)
                            queue.append(None)
                        else:
                            tmp.append(node.right.val)
                            queue.append(node.right)

                return tmp 

    def deserialize(self, data, flag=1):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if len(data) < 1:
            return None
        else:
            if flag in [1,2]:
                root = TreeNode(data[0])
                stack = [root]
                branch = [0]
                i = 1
                while i < len(data) and len(stack) > 0:
                    if branch[-1] < 2:
                        if data[i] is not None: 
                            x = TreeNode(data[i])
                            if branch[-1] == 0: stack[-1].left = x
                            if branch[-1] == 1: stack[-1].right = x
                            stack.append(x)
                            branch[-1] += 1
                            branch.append(0)
                        else:
                            branch[-1] += 1
                        i += 1
                    else:
                        stack.pop()
                        branch.pop()
                return root
            if flag == 3:
                root = TreeNode(data[0])
                queue = [root]
                i = 1
                while len(queue) > 0 and i < len(data):
                    node = queue.pop(0)
                    if node is None:
                        i += 1
                    else:
                        if data[i] is not None:
                            node.left = TreeNode(data[i])
                            queue.append(node.left)
                        if data[i+1] is not None:
                            node.right = TreeNode(data[i+1])
                            queue.append(node.right)
                        i += 2
                return root

# Your Codec object will be instantiated and called as such:
#root = build_tree_bfs( TreeNode(), [0,1,2,3,4,5,6,7,8,9] )
#print_tree_bfs(root)

codec = Codec()
#s = codec.serialize(root, flag=3) 
#print_series(s)
#s = codec.serialize(root, flag=2) 
#print_series(s)

s = [7, 8, None, None, 4, 5, 9, None, 1, 6, 2, None, 0, None, None, None, 3, None, None, None, None]
root = codec.deserialize(s, flag=1)
s3 = codec.serialize(root, flag=3) 

print(s3)
root3 = codec.deserialize(s3, flag=3)
print(codec.serialize(root3, flag=3))




#import random
#random.shuffle(s)
#while (s[0] is None) or (s[-1] is not None):
#    random.shuffle(s)

#print_series(s)
#root3 = codec.deserialize(s)
#print_tree_bfs(root3)

# codec.deserialize(codec.serialize(root))


