#Array vs Dictionary
#To search an element by value in array => O(n)
#To search an element by value in dictionary => O(1)
#Dictionary uses the concept of hashtables
#In hash map you have a string index
#ASCII method used in defining the hash ftn
#Deletion/Insertion => O(1)

def hash_ftn(key): #key is the string
    h = 0
    for char in key:
        h+= ord(char) #ord ftn will find the ASCII value 
    return h%100 

print(ord('m'))
print(hash_ftn('march 6'))

class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)] #created an empty array of the MAX size defined
    
    def hash_ftn(self,key): #key is the string
        h = 0
        for char in key:
            h+= ord(char) #ord ftn will find the ASCII value 
        return h % self.MAX 
    
    def __setitem__(self,key,value): #__setitem__ will execute t['march 6'] = 130 directly
        h = self.hash_ftn(key)
        self.arr[h] = value
    
    def __getitem__(self,key): #__getitem__ will execute t['march 6'] directly and give the value at that date
        index = self.hash_ftn(key)
        return self.arr[index]
    
    def __delitem__(self,key):
        index = self.hash_ftn(key)
        self.arr[index] = None


t = HashTable()
#t.add('march 6' , 130)
t['march 8'] = 560
print(t.arr)
#print(t.get('march 6'))
print(t['march 8'])
#print(t.hash_ftn('march 9'))
del t['march 8']
print(t.arr)


