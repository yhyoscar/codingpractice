

class LLnode:
    def __init__(self, value=None, next=None, pre=None):
        self.value = value
        self.next = next
        self.pre = pre
        return

    def add_nodes(self, array):
        tmp = self
        for x in array:
            node = LLnode(value=x)
            tmp.next = node
            node.pre = tmp
            tmp = tmp.next
        return

    def print_all(self):
        tmp = self
        while tmp is not None:
            print(tmp.value, end=' <-> ')
            tmp = tmp.next
        print('END')
        return

def remove(head, value):
    p1 = head
    p2 = head.next
    if p1.value == value:
        head = head.next
        head.pre = None
    else:
        while p2 is not None:
            if p2.value == value:
                p1.next = p2.next
                if p2.next is not None: p2.next.pre = p1
                return head
            p1 = p1.next
            p2 = p2.next
    return head

s = [5,6,7,8,8,9]
ll = LLnode(value=s[0])
ll.add_nodes(s[1:])
ll.print_all()

ll = remove(ll, 8)
ll.print_all()
ll = remove(ll, 9)
ll.print_all()
ll = remove(ll, 5)
ll.print_all()





