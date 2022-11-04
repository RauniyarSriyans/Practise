# Implement queue using stacks 

class Queue:

    def __init__(self):
        self.enqueue_stack = []
        self.dequeue_stack = []

    def enqueue(self, data):
        self.enqueue_stack.append(data)
    
    def is_empty(self):
        return(len(self.enqueue_stack)==0 and len(self.dequeue_stack)==0)

    def dequeue(self):
        if self.is_empty():
            raise Exception("Empty Queue")
        if len(self.dequeue_stack) == 0:
            while len(self.enqueue_stack) != 0:
                self.dequeue_stack.append(self.enqueue_stack.pop())
        return self.dequeue_stack.pop()

    def queue_size(self):
        return (len(self.enqueue_stack)+ len(self.dequeue_stack))
    
    def peek(self):
        if self.is_empty():
            raise Exception("Empty Queue")
        if len(self.dequeue_stack) != 0:
            return self.dequeue_stack[-1] 
        else:
            return self.enqueue_stack[0]
        
if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.queue_size())
    print(queue.peek())
    
