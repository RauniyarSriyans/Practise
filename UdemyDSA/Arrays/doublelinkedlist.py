from hashlib import new
from traceback import print_tb
from urllib.request import AbstractBasicAuthHandler


class Node:
    
    def __init__(self, data):
        self.data = data 
        self.previous_node = None
        self.next_node = None 

class doubleLinkedList:

    def __init__(self):
        self.head = None 
        self.tail = None
        self.no_of_nodes = 0
    
    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.no_of_nodes += 1
        else:
            new_node.previous_node = self.tail
            self.tail.next_node = new_node
            self.tail =  new_node
            self.no_of_nodes += 1

    def insert_first(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            self.no_of_nodes += 1
        else:
            new_node.next_node = self.head
            self.head.previous_node = new_node
            self.head = new_node
            self.no_of_nodes += 1
    
    def remove_front(self):
        if self.head is None:
            return 
        
        if self.head.next_node is None:
            self.head = None 
            self.no_of_nodes = self.no_of_nodes - 1
        else:
            self.head = self.head.next_node
            self.head.previous_node = None
            self.no_of_nodes = self.no_of_nodes - 1 

    def remove_last(self):
        if self.tail is None or self.head is None:
            return
        
        if self.head.next_node is None:
            self.head = None
            self.no_of_nodes = self.no_of_nodes - 1
        else:
            self.tail = self.tail.previous_node
            self.tail.next_node = None 
            self.no_of_nodes = self.no_of_nodes - 1
    
    def remove_item(self, data):
        if self.head is None or self.tail is None or data is None:
            return 
        
        curr_node = self.head

        while(curr_node is not None and curr_node.data != data):
            curr_node = curr_node.next_node

        if curr_node is None:
            return 
        
        if curr_node.previous_node is None:
            self.head = curr_node.next_node
            self.head.previous_node = None
            self.no_of_nodes = self.no_of_nodes - 1
        elif curr_node.next_node is None:
            self.tail = curr_node.previous_node
            self.tail.next_node = None 
            self.no_of_nodes = self.no_of_nodes - 1
        else:
            curr_node.previous_node.next_node = curr_node.next_node
            curr_node.next_node.previous_node = curr_node.previous_node
            self.no_of_nodes = self.no_of_nodes - 1
    
    def traverse_forward(self):
        curr_node = self.head

        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next_node
    
    def traverse_backward(self):
        curr_node = self.tail

        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.previous_node

    def numberOfNodes(self):
        return self.no_of_nodes

if __name__ == '__main__':

    my_list = doubleLinkedList()
    my_list.insert_first('First')
    my_list.insert_end('Second')
    my_list.insert_end('Third')
    my_list.insert_end('Fourth')
    my_list.traverse_forward()
    print()
    my_list.traverse_backward()
    print()

    my_list.remove_front()
    my_list.traverse_forward()
    print()
    my_list.traverse_backward()
    print()

    my_list.remove_last()
    my_list.traverse_forward()
    print()
    my_list.traverse_backward()
    print()

    my_list.insert_end('Fourth')
    my_list.insert_end('Fifth')
    my_list.insert_first('First')
    my_list.traverse_forward()
    print()
    
    my_list.remove_item('Third')
    my_list.traverse_backward()
    print()
    my_list.traverse_forward()
    print()