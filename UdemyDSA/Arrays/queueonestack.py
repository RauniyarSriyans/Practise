# Implementing queue using one single stack 

class Queue:

    def __init__(self):
        self.stack = []

    def enqueue(self, data):
        self.stack.append(data)

    # using recursion
    def dequeue(self):
        # base case for the recursive method calls
        if len(self.stack) == 1:
            return self.stack.pop()
        # keep popping until you find the last one
        item = self.stack.pop()
        # call the method recursivelt unril we find the first item 
        dequeued_item = self.dequeue()
        # after finding the item, reinsert one by one
        self.stack.append(item)
        return dequeued_item
