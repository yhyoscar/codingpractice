
class Element:
    def __init__(self, value, pre=None, next=None):
        self.value = value
        self.pre = pre
        self.next = next
        return

class LL:
    def __init__(self):
        self.length = 0

    def add(self, e):
        if self.length == 0:
            self.head = e
            self.tail = e
        else:
            self.tail.next = e
            self.tail = e
        self.length += 1
        return

    def display(self):
        pointer = self.head
        for i in range(self.length):
            print(pointer.value, ' -> ')
            if i<self.length-1: pointer = pointer.next
        return

if __name__ == '__main__':
    q = LL()
    s = ['a', 1, 'bc']
    for i in s:
        q.add(Element(i))

    q.display()

