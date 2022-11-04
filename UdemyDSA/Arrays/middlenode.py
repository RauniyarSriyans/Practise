# Suppose we have a standard linked list. Construct an in-place 
# (without extra memory) algorithm thats able to find the middle node!

# is a method in the previous linkedlist implementation 
class linkedlist:

    def getMiddleNode(self):
        fast_pointer = self.head
        slow_pointer = self.head 

        while fast_pointer.next_node is not None and fast_pointer.next_node.next_node is not None:
            fast_pointer = fast_pointer.next_node.next_node 
            slow_pointer = slow_pointer.next_node 

        return slow_pointer

