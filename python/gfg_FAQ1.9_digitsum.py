#Given two numbers represented by two lists, write a function that returns sum list. The sum list is list representation of addition of two input numbers.

#Input:
#      First List: 5->6->3  // represents number 365
#        Second List: 8->4->2 //  represents number 248
#        Output
#          Resultant list: 3->1->6  // represents number 613


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        return

def add_node(head, value):
    if head.value is None:
        head.value = value
    else:
        tmp = head
        while tmp.next:
            tmp = tmp.next
        tmp.next = Node(value)
    return

def printLL(head):
    tmp = head
    while tmp:
        print(tmp.value)
        tmp = tmp.next
    return

def sumll(head1, head2):
    d1 = head1
    d2 = head2
    flag = 0
    s = Node()
    while (d1 is not None) or (d2 is not None):
        v = flag
        if d1 is not None:
            v += d1.value
            d1 = d1.next
        if d2 is not None:
            v += d2.value
            d2 = d2.next

        add_node( s, int(v % 10) )
        flag = int( v//10 )

    return s



if __name__ == '__main__':
    head1 = Node()
    add_node(head1, 7)
    add_node(head1, 6)
    add_node(head1, 5)
    printLL(head1)

    head2 = Node()
    add_node(head2, 5)
    add_node(head2, 4)
    add_node(head2, 3)
    add_node(head2, 2)
    printLL(head2)
   
    s = sumll(head1, head2)
    printLL(s)


