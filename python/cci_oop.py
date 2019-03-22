# inheritance

class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        return

    def name(self):
        return self.first + ', '+self.last

class Employee(Person):
    def __init__(self, first, last, id):
        Person.__init__(self, first, last)
        self.id = id
        return

class Employer(Person):
    def __init__(self, first, last, level):
        Person.__init__(self, first, last)
        self.level = level
        return
    

if __name__ == '__main__':
    alice = Employee(first='Alice', last='Robert', id=2)
    oscar = Employer(first='Oscar', last='Yu', level=10)

    print(alice.name())
    print(oscar.name())
