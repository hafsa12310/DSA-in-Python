class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child_node(self, child):
        child.parent = self
        self.children.append(child)
    
    def get_level(self):
        #count number of parents to determine the level pf each node
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self):
        spaces = '' + str(self.get_level())*3 #each level = no of level*3 spaces
        prefix = spaces + "|__" if self.parent else ""
        print (prefix + self.data)
        if len(self.children) > 0:

            for child in self.children:
                child.print_tree()


def build_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child_node(TreeNode("Mac"))
    laptop.add_child_node(TreeNode("Dell"))

    mobile = TreeNode("mobile")
    mobile.add_child_node(TreeNode("samsung"))
    mobile.add_child_node(TreeNode("Redmi"))

    root.add_child_node(laptop)
    root.add_child_node(mobile)

    #print (mobile.get_level())
    return root


root = build_tree()
root.print_tree()