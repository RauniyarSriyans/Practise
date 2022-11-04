class Node:

    def __init__(self, data, parent = None):
        self.data = data 
        self.parent_node = parent
        self.right_child = None
        self.left_child = None

class BinarySearchTree:

    def __init__(self):
        self.root = None 
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, node):
        

        



    