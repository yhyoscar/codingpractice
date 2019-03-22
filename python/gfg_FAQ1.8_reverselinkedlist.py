# Given a linked list, write a function to reverse every k nodes (where k is an input to the function).

# Example:
#    Inputs:  1->2->3->4->5->6->7->8->NULL and k = 3 
#    Output:  3->2->1->6->5->4->8->7->NULL. 


class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next
        return

class LinkedList:
    def __init__(self, head=None):
        self.head = head
        return

    def printLL(self):
        tmp = self.head
        while (tmp):
            print(tmp.value)
            tmp = tmp.next
        return

    def add_node(self, value):
        if self.head is None:
            self.head = Node(value=value)
        else:
            tmp = self.head
            while tmp.next:
                tmp = tmp.next
            tmp.next = Node(value=value)
        return

def reverse(head, k):
    pa = head
    pb = head.next
    pre = None
    while (pa is not None and pb is not None):
        first = pa
        count = 0
        while count < k-1 and (pb is not None):
            tmp = pb.next
            pb.next = pa
            pa = pb
            pb = tmp
            count += 1
        first.next = pb
        if pre is not None:
            pre.next = pa
        else:
            head = pa
        
        pre = first
        pa = pb
        if pb is not None: pb = pb.next
    return head


if __name__ == '__main__':
    ll = LinkedList()
    for i in range(1,11):
        ll.add_node(i)
    ll.printLL()
    print('reverse: ')
    ll = LinkedList( head = reverse(ll.head, k=3) )
    ll.printLL()


