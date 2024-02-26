#Queue allows you to establish loose coupling
#follows FIFO
#List can be used as a queue in Python

queue  = []

queue.insert(0,12)
queue.insert(0,13)
queue.insert(0,14)
print(queue)

queue.pop()
print(queue)

#Using list is not very much recommended to be used as the queue as the same problem arises => O(n)

from collections import deque
q = deque()

q.appendleft(4)
q.appendleft(5)
q.appendleft(6)
q.appendleft(7)

print(q)

print(q.pop())

class Queue:

    def __init__(self):
        self.buffer = deque()

    def enqueue(self, value):
        self.buffer.appendleft(value)
    
    def dequeue(self):
        return self.buffer.pop()
    
    def is_empty(self):
        return len(self.buffer)==0
    
    def size(self):
        return len(self.buffer)