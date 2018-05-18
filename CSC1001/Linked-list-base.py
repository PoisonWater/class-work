class Node:
    def __init__(self,element,pointer):
        self.element = element
        self.pointer = pointer

class LinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_first(self,e):
        newest = Node(e,None)
        newest.pointer = self.head
        self.head = newest
        self.size = self.size+1

        if self.size == 1:
            self.tail = newest

    def add_last(self,e):
        newest = Node(e,None)
        self.tail.pointer = newest
        self.tail = newest
        self.size = self.size+1

    def remove_first(self):
        if self.size == 0:
            print('The linked list is empty')
        else:
            self.head = self.head.pointer
            self.size = self.size - 1
        
ll = LinkedList()
ll.add_first(10)
ll.add_last(20)
ll.add_last(30)
    

##class LinkedStack:
##    
##    def __init__(self):
##        self.head = None
##        self.size = 0
##
##    def __len__(self):
##        return self.size
##
##    def is_empty(self):
##        return self.size == 0
##
##    def push(self,e):
##        self.head = Node(e,self.head)
##        self.size+=1
##
##    def top(self):
##        if self.is_empty():
##            print('Stack is empty')
##        else:
##            return self.head.element
##
##    def pop(self):
##        if self.is_empty():
##            print('Stack is empty')
##        else:
##            answer = self.head.element
##            self.head = self.head.pointer
##            self.size-=1
##            return answer
##
##ls = LinkedStack()
##ls.push(100)
##ls.push(200)
##ls.push(300)
##print(ls.__len__())
##print(ls.top())
##print(ls.pop())

##class LinkedQueue:
##
##    def __init__(self):
##        self.head = None
##        self.tail = None
##        self.size = 0
##
##    def __len__(self):
##        return self.size
##
##    def is_empty(self):
##        return self.size == 0
##
##    def first(self):
##        if self.is_empty():
##            print('Queue is empty')
##        else:
##            return self.head.element
##
##    def dequeue(self):
##        if self.is_empty():
##            print('Queue is empty')
##        else:
##            answer = self.head.element
##            self.head = self.head.pointer
##            self.size-=1
##            if self.is_empty():
##                self.tail = None
##            return answer
##
##    def enqueue(self,e):
##        newest = Node(e,None)
##
##        if self.is_empty():
##            self.head = newest
##        else:
##            self.tail.pointer = newest
##        self.tail = newest
##        self.size+=1
##
##lq = LinkedQueue()
##lq.enqueue(10)
##lq.enqueue(20)
##lq.enqueue(30)
##print(lq.first())
##print(lq.dequeue())
##print(lq.first())

    

