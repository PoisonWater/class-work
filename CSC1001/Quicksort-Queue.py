## Define class ListQueue, representing a queue.
class Node:
    def __init__(self, element, pointer):
        self.element = element
        self.pointer = pointer

class LinkedQueue:

    def __init__(self):
        self.head = None
        self.size = 0
        self.tail = None

    def __len__(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def first(self):
        if self.is_empty():
            print('Queue is empty.')
        else:
            return self.head.element

    def dequeue(self):
        if self.is_empty():
            print('Queue is empty.')
        else:
            answer = self.head.element
            self.head = self.head.pointer
            self.size -= 1
            if self.is_empty():
                self.tail = None
            return answer

    def enqueue(self,e):
        newest = Node(e,None)
        if self.is_empty():
            self.head = newest
        else:
            self.tail.pointer = newest
        self.tail = newest
        self.size += 1
    
    def show(self):
        return self.head

p_time = 1

def count(at):
    global p_time
    if at.pointer != None:
        p_time += 1
        count(at.pointer)
    else:
        return p_time 

standardQ = LinkedQueue()
## Quick sort method
def quickSort_0(Q):
    global standardQ
    key = Q.dequeue()
    Qa = LinkedQueue()
    Qb = LinkedQueue()
    Qc = 1
    for i in range(Q.__len__()):
        t = Q.dequeue()
        if t == key:
            Qc += 1
        elif t < key:
            Qb.enqueue(t)
        elif t > key:
            Qa.enqueue(t)
    if not Qb.is_empty():
        quickSort_0(Qb)
    for i in range(Qc):
        standardQ.enqueue(key)
    if not Qa.is_empty():
        quickSort_0(Qa)

def quickSort(a):
    global standardQ
    p = a
    if type(a) == Node:
        Q = LinkedQueue()
        Q.head = a
        Q.size = p_time
        for i in range(Q.size-1):
            c = p.pointer
        Q.tail = p.element
        standardQ = LinkedQueue()
        quickSort_0(Q)
        return standardQ.show()
    else:
        print('Wrong input! You need to input a node!')

Q = LinkedQueue()
for i in [7,3,7,7,2,6,1,8,4,5,9]:
    Q.enqueue(i)
t = quickSort(Q.head)
print(t)