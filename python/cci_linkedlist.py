class LLnode:
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

def delete_node(node):
    if node.next is None:
        return
    else:
        p = node
        while p.next is not None:
            if p.next.next is None: pend = p
            p.value = p.next.value
            p = p.next
        pend.next = None
        return

def add_digit(head1, head2):
    p1 = head1; p2 = head2; headout=LLnode(value=0); pout = headout; carry = 0
    while True:
        if p1 is not None: pout.value += p1.value; p1=p1.next
        if p2 is not None: pout.value += p2.value; p2=p2.next
        carry =  pout.value // 10
        pout.value = pout.value % 10
        if (p1 is None and p2 is None and carry==0): break
        else: pout.next = LLnode(value=carry); pout=pout.next
    return headout

if __name__ == '__main__':
    head = LLnode(value=0); add_nodes(head, range(1,13)); print_ll(head)
    node=head  
    for i in range(11): node=node.next; 
    delete_node(node); print_ll(head)

    s=[4,5,9,9]; head1 = LLnode(value=s[0]); add_nodes(head1, s[1:])
    s=[6,7,2]; head2 = LLnode(value=s[0]); add_nodes(head2, s[1:])
    headout = add_digit(head1, head2); print_ll(head1); print_ll(head2); print_ll(headout)


