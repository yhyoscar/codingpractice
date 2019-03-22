# Design an algorithm and write code to find the first common ancestor of two nodes in a binary tree. Avoid storing additional nodes in a data structure. NOTE: This is not necessarily a binary search tree.

from cci_tree import TreeNode

# loop for node1:
#   loop for node2:
#       if node2 == node1: return
#       else: node2 = node2.parent
#   node1 = node1.parent
def firstancestor(root, node1, node2):
    p1 = node1
    while not (p1 is None) :
        p2 = node2
        while not (p2 is None) :
            if p1.value == p2.value:
                return p1
            else:
                p2 = p2.parent
        p1 = p1.parent
    return None

if __name__ == '__main__':
    s = [4,2,5,1,3,7,6]
    root = TreeNode(s[0])
    root.create_tree(s[1:])
    node1 = root.left.left
    node2 = root.right
    ancestor = firstancestor(root, node1, node2)
    print(node1.value, node2.value)
    if ancestor is None:
        print('None')
    else:
        print(ancestor.value)



