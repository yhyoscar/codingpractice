# Implement a function to check if a tree is balanced. For the purposes of this question, a balanced tree is defined to be a tree such that no two leaf nodes differ in distance from the root by more than one.

# 1. get the depths for all leaves
# 2. if max(d)-min(d)<=1: balanced

from cci_tree import TreeNode

# depth list = left list + right list
def depth_list(node, dlist, d):
    if node.left is None and node.right is None:
        dlist[node.value] = d
    else:
        if not (node.left is None):
            depth_list(node.left, dlist, d+1)
        if not (node.right is None):
            depth_list(node.right, dlist, d+1)
    return

def is_balanced(root):
    dlist = {}
    depth_list(root, dlist, 0)
    if (max(dlist.values()) - min(dlist.values())) <= 1:
        return True
    else:
        return False

if __name__ == '__main__':
    s = [4,5,2,1,6,7,3]
    root = TreeNode(value=s[0])
    root.create_tree(s[1:])
    dlist = {}
    depth_list(root, dlist, 0)
    print(dlist)
    print('balanced: ', is_balanced(root))


