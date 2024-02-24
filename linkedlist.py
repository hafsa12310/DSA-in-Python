#O(n) complexity

def square_numbers(numbers):
    squared_list = []
    for i in numbers:
        squared_list.append(i*i)
    return squared_list

numbers = [2,3,4,5,7] 
print(square_numbers(numbers))

#O(1) complexity => no loop

def find_fidt_pe(prices, eps, index):
    pe = prices[index]/eps[index]
    return pe

#O(n^2) complexity => 2 loops

numbers = [1,2,3,4,5,6]
for i in range(len(numbers)):
    for j in range(i+1, len(numbers)):
        if numbers[i] == numbers [j]:
            print ("Duplicate found")
            break

#O(log n) complexity => binary search
#O(n) complexity => linear search
        

#Inserting in an array
#Complexity is O(n) since doing all the swaps
        
array = [1,2,3,4,5,6,7,8,9,10]
print(array)

array.insert(1,284) #insertion will increase the size of the array. each value moves one step ahead
print(array)

#Deleting from the array
#Complexity is again O(n)

array.remove(5)
print(array)

#List/Array Exercises

expenses = [2200, 2350, 2600, 2130, 2190]
extra = expenses[1] - expenses[0]
print (extra)

expenses_dict = {
    'Jan' : 2200,
    'Feb' : 2350,
    'March' : 2600,
    'April' : 2130,
    'May' : 2190
}

extra_expense = expenses_dict['Feb'] - expenses_dict['Jan']
print(extra_expense)

#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

odd_numbers = []
print("Enter the max number")
max_number = int(input()) 
for i in range(max_number+1):
    if (i%2 != 0):
        odd_numbers.append(i)

print(odd_numbers)

#Linked List

#complexity of O(n) => insertion/deletion at end/middle
#complexity of O(1) => insertion/deletion at start

#representing individual element in the linked list
class Node:         
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None    #pointing to the head of the linked list

    def insert_in_start(self, data):
        node = Node(data,self.head) #self.head => next value of the node is the CURRENT head 
        self.head = node
    
    def print(self):
        if self.head is None:
            print("Empty")
            return
    
        itr = self.head
        llist = ''
        while itr:
            llist += str(itr.data) + '-->'
            itr = itr.next
        print(llist)
    
    def insert_in_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next #keep iterating till the next is pointing to Null
        
        itr.next = Node(data,None) #create a new node when the next =>Null is found

#ist of value as input and creating a new linked list
    
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_in_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next
        return count

#Remove an element at a given index
    
    def remove_at(self,index):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1
    
    def insert_at(self,index,data):
        if index<0 or index>=self.get_length():
            raise Exception("Invalid Index")
        
        if index==0:
            self.insert_in_start(data)
            return
        
        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                n1 = Node(data, itr.next)
                itr.next = n1
                break
            itr = itr.next
            count +=1

#Linked List Exercise-Insertion/Deletion after a value

    def insert_after_value(self, data, data1):

        if data == self.head.data:
            n1 = Node(data1, self.head.next)
            self.head.next = n1
            return
        
        itr = self.head
        while itr:
            if itr.data == data:
                n2 = Node(data1, itr.next)
                itr.next = n2
                break
            itr = itr.next
    
    def delete_on_value (self, data):

        if data == self.head.data:
            self.head = self.head.next
            return
        
        iter = self.head
        while iter.next:
            if iter.next.data == data:
                iter.next = iter.next.next
                break
            itr = itr.next

#Double Linked List 

class Double_Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev

class Double_Linked_List:

    def __init__(self):
        self.head = None
    
    def insert_in_end(self,data):
        if self.head is None:
            self.head = Double_Node(data,None,None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next #keep iterating till the next is pointing to Null
            
        itr.next = Double_Node(data,None,None) #create a new node until the next =>Null is found

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_in_end(data)

    def print_forward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        itr = self.head
        llstr = ''
        while itr:
            llstr += str(itr.data) + ' --> '
            itr = itr.next
        print(llstr)

    
    def get_last_node(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr
    
    
    def print_backward(self):
        if self.head is None:
            print("Linked list is empty")
            return

        last_node = self.get_last_node()
        itr = last_node
        self.head = itr
        llstr = ''
        while itr:
            llstr += itr.data + '-->'
            itr = itr.prev
        print(llstr)



ll = LinkedList()
ll.insert_in_start(1)
ll.insert_in_start(2)
ll.insert_in_start(3)
ll.insert_in_end(1)
ll2 = LinkedList()
data = ["a","b","c", "d", "e"]
ll2.insert_values(data)
ll.print()
ll2.print()
print(ll2.get_length())

ll2.remove_at(2)
ll2.print()

ll2.insert_at(2,"c")
ll2.print()

ll2.insert_after_value("a" , "z") #adding a value after the head
ll2.print()

ll2.insert_after_value("c", "x") #adding a value in middle
ll2.print()

ll2.insert_after_value("e", "y") #adding after the tail
ll2.print()

ll2.delete_on_value("z")
ll2.print()

ll3 = Double_Linked_List()
ll3.insert_in_end("hafsa")
ll3.insert_in_end("ok")
ll3.print_forward()

data2 = ["apple","banana","cabbage", "dog", "elephant"]
ll3.insert_values(data2)
ll3.print_forward()

ll3.print_backward()

