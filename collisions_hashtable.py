#collison occurs when the ASCII values of the key come out to be the same
#use the concept of separate chaining
#instead of directly stroing the value we use a linked list/list at every location
#for searching the complexity migth now become O(n) from O(1) since now the list has to be traversed
#Use linear probing instead of chaining
#Here you search for an empty next slot

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [[] for i in range(self.MAX)] #instead of the None element at each index we now have an empty array instead
    
    def hash_ftn(self,key): #key is the string
        h = 0
        for char in key:
            h+= ord(char) #ord ftn will find the ASCII value 
        return h % self.MAX 
    
    def __setitem__(self,key,value): #__setitem__ will execute t['march 6'] = 130 directly
        h = self.hash_ftn(key)
        found = False

        #if key already existed
        for idx, element in enumerate(self.arr[h]):
            if len(element)==2 and element[0] == key:
                self.arr[h][idx] = (key,value) #if the key exists you are just modifying that key,value pair
                found = True
                break
        if not found:
            self.arr[h].append((key,value))


    def __getitem__(self,key): #__getitem__ will execute t['march 6'] directly and give the value at that date
        index = self.hash_ftn(key)
        for element in self.arr[index]:
            if element[0]==key:
                return element[1]
    
    def __delitem__(self,key):
        index = self.hash_ftn(key)
        for idx,element in self.arr[index]:
            if element[0]==key:
                del self.arr[index][idx]


t = HashTable()
t["march 6"] = 420
t["march 6"] = 80
t["march 8"] = 90
t["march 17"] = 100

print(t.arr)

print(t["march 17"])


