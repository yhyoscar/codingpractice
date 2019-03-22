# Binary tree traversal questions like left view, right view, top view, bottom view, maximum of a level, minimum of a level, children sum property, diameter etc.

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left  = left
        self.right = right
        return

# construct a binary search tree from an array
def construct_BST(array):
    n = len(array)
    if n > 0:
        root = Node(value=array[0])
        for i in range(1,n):
            node = Node(value=array[i])
            construct_BST_recur(root, node)
    else:
        root = None
    return root

def construct_BST_recur(root, node):
    if root is not None:
        if node.value < root.value:
            if root.left is None:
                root.left = node
            else:
                construct_BST_recur(root.left, node)
        else:
            if root.right is None:
                root.right = node
            else:
                construct_BST_recur(root.right, node)
    return 

# tree to doubly lined list
def tree_to_dll(root, head):
    if root is not None:
        tree_to_dll(root.left, head)
        insert_node(head, root)
        tree_to_dll(root.right, head)
    return 

# insert a new node to a doubly linked list
def insert_node(head, node):
    if head is not None:
        if head.value is None:
            head.value = node.value
        else:
            if head.right is None:
                head.right = Node(value=node.value)
                head.right.left = head
            else:
                insert_node(head.right, node)
    return

# traverse a linked list
def print_LL(head):
    if head is not None:
        print(head.value)
        print_LL(head.right)
    return


if __name__ == '__main__':
    root = construct_BST([4,2,6,0,3,5,8,7,1])
    head = Node()
    tree_to_dll(root, head)
    print_LL(head)
