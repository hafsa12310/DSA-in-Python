#Stack follows LIFO
#Push/Pop => O(1)
#Search an element => O(n)
#Stack is used to manage the ftn calls
#Python list can bes used as a stack

s = []
s.append('a')
s.append('b')
s.append('c')
s.append('d')
s.append('e')

print(s)
s.pop()
print(s)

print(s[-1]) #-1 used to get the last element in python

#Instead of using list as a stack in python use collections.deque
#Imlpementation of stack using deque

from collections import deque

stack = deque()
print(dir(stack))

stack.append('f')
stack.append('g')
stack.append('h')
stack.append('i')
print(stack)
print(stack.pop())
print(stack)

class Stack:

    def __init__(self):
        self.s = deque()

    def enqueue(self, value):
        self.s.append(value)
    
    def dequeue(self):
        return self.s.pop()
    
    def is_empty(self):
        return len(self.s)==0
    
    def size(self):
        return len(self.s)

