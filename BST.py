#sets remove the duplicates
x = set(['Hafsa', 'Hafsa', 'x', 'y' ,'z', 'z'])
print(x)

#to implement set you can use BST 
#BST is a special type of binary tree where elements have an order
#elements are not duplicated
#we reduce search space by half everytime
#search complexity => O(log n)
#insert complexity => O(log n)
#visit left subtree first then right subtree

class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def add_child(self, data):
        if data == self.data:
            return      #since BST cant have duplicates
        
        if data < self.data:
            #add data to left subtree
            if self.left:
                self.left.add_child(data) #recursion 
            else:
                self.left = BST(data)
        else:
            #add data to right subtree
            if self.right:
                self.right.add_child(data) #recursion 
            else:
                self.right = BST(data)
    
    def inorder_traversal(self):
        elements = []

        #include left subtree

        if self.left: #if you have elements in the left this is being checked
            elements += self.left.inorder_traversal()
        
        #include root node
        
        elements.append(self.data)

        #include right subtree
        if self.right: #if you have elements in the right this is being checked
            elements += self.right.inorder_traversal()
        
        return elements
    
    def search(self,val):

        if self.data == val:
            return self.data
        
        if val < self.data:
            if self.left:
                return self.left.search(val)
            
            else:
                return False
            
        
        if val > self.data:
            if self.right:
                return self.right.search(val)
            else:
                return False
    
    def min(self):
        
        if self.left:
            return self.left.min()
        
        #elif self.right:
            #return self.right.min()
        
        else:
            return self.data
        
    def max(self):

        if self.right:
            return self.right.max()
        
        else:
            return self.data
    
    def delete(self,value):
        
        if value < self.data:
            if self.left:
                self.left = self.left.delete(value)
            else:
                return None
            
        elif value > self.data:
            if self.right:
                self.right = self.right.delete(value)
        
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left
            
            min_val = self.right.min()
            self.data = min_val
            self.right = self.right.delete(min_val)
        
        return self


def build_tree(elements):
    print("Building tree with these elements:",elements)
    root = BST(elements[0])

    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root


countries = ["India","Pakistan","Germany", "USA","China","India","UK","USA"]
country_tree = build_tree(countries)

print("UK is in the list? ", country_tree.search("UK"))
print("Sweden is in the list? ", country_tree.search("Sweden"))

numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
print("In order traversal gives this sorted list:",numbers_tree.inorder_traversal())

print(numbers_tree.min())
print(numbers_tree.max())

numbers_tree.delete(20)
print(numbers_tree.inorder_traversal())