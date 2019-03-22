ass LLnode:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        return

def add_nodes(head, array):
    current = head
    for x in array:
        current.next = LLnode(value=x)
        current = current.next
    return

def print_ll(head):
    p = head
    while p is not None:
        print(p.value, end=' -> ')
        p = p.next
    print('END')
    return

head = LLnode(value=0)
Add_nodes(head, [1,2,3,4,4,5,4]); print_ll(head)


de(head, value):
    p = head
    pre = None
    while not (p is None):
        if p.value != value:
            pre = p
            p = p.next            
        else:
            break
    if p is None:
        print(value, ' does not exist!')
        return head
    else:
        if p.value == head.value:
            return head.next
        if p.next is None:
            p = None
        else:
            pre.next = p.next
        return head

head = delete_node(head, 2)
print_ll(head)
head = delete_node(head, 1)
print_ll(head)
head = delete_node(head, 4)
print_ll(head)


d = LLnode(value=0)
add_nodes(head, [0,1,2,3,4,4,5,4]); print_ll(head)

def delete_duplicate(head):
    p = head
    pre = None
    s = []
    while not (p is None):
        print(s)
        if p.value not in s:
            s.append(p.value)
            pre = p
            p = p.next            
        else:
            p = p.next
            pre.next = p

    return head

head = delete_duplicate(head)
Print_ll(head)
