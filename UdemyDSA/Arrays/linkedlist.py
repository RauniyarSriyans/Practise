class Node:

    def __init__(self, data):
        self.data = data
        self.next_node = None 

class LinkedList:

    def __init__(self):
        self.head = None
        self.no_of_nodes = 0
    
    def insert_start(self, data):
        new_node = Node(data)
        self.no_of_nodes += 1

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node
    
    def insert_last(self, data):
        new_node = Node(data)
        self.no_of_nodes += 1

        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while(curr_node.next_node is not None):
                curr_node = curr_node.next_node
            curr_node.next_node = new_node
    
    def remove(self, data):
        if self.head is None or data is None: 
            return

        curr_node = self.head
        previous_node = None

        while(curr_node is not None and curr_node.data != data):
            previous_node = curr_node
            curr_node = curr_node.next_node

        if curr_node is None:
            return
        
        if previous_node is None:
            self.head = curr_node.next_node
            self.no_of_nodes -= 1
        else:
            previous_node.next_node = curr_node.next_node
            self.no_of_nodes -= 1
    
    def getMiddleNode(self):
        fast_pointer = self.head
        slow_pointer = self.head 

        while fast_pointer.next_node and fast_pointer.next_node.next_node:
            fast_pointer = fast_pointer.next_node.next_node 
            slow_pointer = slow_pointer.next_node 

        return slow_pointer

    # Reverses the singly linked list in place in O(N) complexity
    def inPlaceReversal(self):
        if self.head is None:
            return 
        curr_node = self.head
        previous_node, next_node = None, None 

        while curr_node is not None:
            next_node = curr_node.next_node
            curr_node.next_node = previous_node
            previous_node = curr_node
            curr_node = next_node
        self.head = previous_node


    def size_of_list(self):
        return self.no_of_nodes

    def traverse(self):
        curr_node = self.head
        while(curr_node is not None):
            print(curr_node.data)
            curr_node = curr_node.next_node

if __name__ == '__main__':
    my_list  = LinkedList()
    my_list.insert_start(10)
    my_list.insert_last('Adam')
    my_list.insert_last(7.4)
    my_list.traverse()
    print(my_list.size_of_list())
    my_list.remove('Adam')
    my_list.traverse()
    print(my_list.size_of_list())

    my_list2 = LinkedList()
    my_list2.insert_start(10)
    my_list2.insert_last(20)
    my_list2.insert_last(30)
    my_list2.insert_last(40)
    my_list2.insert_last(50)
    my_list2.traverse()
    print(my_list2.getMiddleNode().data)