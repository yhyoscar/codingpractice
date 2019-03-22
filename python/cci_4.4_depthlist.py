# Given a binary search tree, design an algorithm which creates a linked list of all the nodes at each depth (i.e., if you have a tree with depth D, you’ll have D linked lists).

from cci_tree import TreeNode

# traverse the tree and append the depth of each node to the lists
def depthlist(node):
    dlist = {}
    if not (node is None):
        depthlist_recur(node, dlist, 0)
    return dlist

def depthlist_recur(node, dlist, d):
    if not (node is None):
        if d in dlist.keys():
            dlist[d].append(node)
        else:
            dlist[d] = [node]
        if not (node.left is None):
            depthlist_recur(node.left, dlist, d+1)
        if not (node.right is None):
            depthlist_recur(node.right, dlist, d+1)
    return

if __name__ == '__main__':
    s = [4,5,2,1,6,7,3]
    root = TreeNode(value=s[0])
    root.create_tree(s[1:])
    dlist = depthlist(root)
    for i in dlist.keys():
        print('depth = ', i)
        for node in dlist[i]:
            print(node.value)

