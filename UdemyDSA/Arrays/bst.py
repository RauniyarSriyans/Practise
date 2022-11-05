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
        # if data is less than node.data
        if data < node.data:
            if node.left_child:
                # if left child exists, recursively call insert_node
                self.insert_node(data, node.left_child)
            else:
                # if left child does not exist, create a new node
                node.left_child = Node(data, node)
        else:
            if node.right_child:
                # if right child exists, recursively call insert_node
                self.insert_node(data, node.right_child)
            else:
                # if right child does not exist, create a new node
                node.right_child = Node(data, node)
    
    def remove(self, data):
        if self.root:
            self.remove_node(data, self.root)
    
    def remove_node(self, data, node):
        # first we have to find the node we want to remove 
        if node is None:
            return
        
        if data < node.data:
            self.remove_node(data, node.left_child)
        elif data > node.data:
            self.remove_node(data, node.right_child)
        else:
            # Case 1: if the node found is a leaf node
            if node.left_child is None and node.right_child is None:
                parent = node.parent_node 
                if parent is not None and parent.left_child == node:
                    parent.left_child = None 
                elif parent is not None and parent.right_child == node:
                    parent.right_child = None
                elif parent is None:
                    self.root = None 
                del node
            # Case 2a: if the node has a single right child 
            elif node.left_child is None and node.right_child is not None:
                parent = node.parent_node
                if parent is not None and parent.left_child == node:
                    parent.left_child = node.right_child 
                elif parent is not None and parent.right_child == node:
                    parent.right_child = node.right_child
                elif parent is None:
                    self.root = node.right_child 
                node.right_child.parent_node = parent
                del node 
            # Case 2b: if the node has a single left child
            elif node.left_child is not None and node.right_child is None:
                parent = node.parent_node 
                if parent is not None and parent.left_child == node:
                    parent.left_child = node.left_child 
                elif parent is not None and parent.right_child == node:
                    parent.right_child = node.left_child
                elif parent is None:
                    self.root = node.left_child 
                node.left_child.parent_node = parent
                del node
            # Case 3: any other node within the tree
            else:
                predecessor = self.get_predecessor(node.left_child)
                temp = predecessor.data
                predecessor.data = node.data
                node.data = temp 
                self.remove(data, predecessor)

    def get_predecessor(self, node):
        currNode = node 
        while currNode.right_child is not None:
            currNode = currNode.right_child 
        return currNode

    def get_min(self):
        if self.root is None:
            return None 
        else:
            node = self.root
            while node.left_child:
                node = node.left_child
        return node.data
            
    def get_max(self):
        if self.root is None:
            return None 
        else:
            node = self.root
            while node.right_child:
                node = node.right_child
        return node.data
    
    def traverse(self):
        if self.root is None:
            return
        self.traverse_in_order(self.root)
        print()
        self.traverse_pre_order(self.root)
        print()
        self.traverse_post_order(self.root)
    
    # left, root, right -> that's the order
    # gives the sorted order
    def traverse_in_order(self, node):
        if node:
            self.traverse_in_order(node.left_child)
            print(node.data)
            self.traverse_in_order(node.right_child)
    
    def traverse_pre_order(self, node):
        if node:
            print(node.data)
            self.traverse_pre_order(node.left_child)
            self.traverse_pre_order(node.right_child)
    
    def traverse_post_order(self, node):
        if node:
            self.traverse_post_order(node.left_child)
            self.traverse_post_order(node.right_child)
            print(node.data)

    # checks if two trees are same or not
    def compareTree(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        elif root1 is None and root2 is not None:
            return False 
        elif root2 is not None and root1 is None:
            return False 
        else:
            if ((root1.data ==root2.data) and self.compareTree(root1.left_child, root2.left_child) and self.compareTree(root1.right_child, root2.right_child)):
                return True 
            else:
                return False
        
if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(27)
    bst.insert(14)
    bst.insert(35)
    bst.insert(10)
    bst.insert(19)
    bst.insert(31)
    bst.insert(42)
    print(bst.get_min())
    print(bst.get_max())
    print()
    print(bst.traverse())
