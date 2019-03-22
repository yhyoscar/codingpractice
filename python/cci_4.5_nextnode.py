# Write an algorithm to find the ‘next’ node (i.e., in-order successor) of a given node in a binary search tree where each node has a link to its parent.

from cci_tree import TreeNode

# traverse the tree in-order, return the node list in order,
# then, search for the given node, and get the next one
def nodelist_inorder(node):
    nodelist = []
    nodelist_inorder_recur(node, nodelist)
    return nodelist

def nodelist_inorder_recur(node, nodelist):
    if not (node is None):
        if not (node.left is None):
            nodelist_inorder_recur(node.left, nodelist)
        nodelist.append(node)
        if not (node.right is None):
            nodelist_inorder_recur(node.right, nodelist)
    return

def findnextnode(root, nodevalue):
    nodelist = nodelist_inorder(root)
    n = len(nodelist)
    for i in range(n):
        if nodelist[i].value == nodevalue:
            break
    if i >= n-1:
        return None
    else:
        return nodelist[i+1].value

if __name__ == '__main__':
    s = [4,2,5,1,3,7,6]
    root = TreeNode(value = s[0])
    root.create_tree(s[1:])
    nodelist = nodelist_inorder(root)
    for node in nodelist:
        print(node.value)
    print('after 7: ', findnextnode(root, 7))


