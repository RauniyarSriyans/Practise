# queue implementation 

class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        # don't do anything if the stack is empty
        if self.queue_size() < 1:
            return 
    
        data = self.queue[0]
        del self.queue[0]
        return data
    
    def peek(self):
        return self.queue[0]
    
    def is_empty(self):
        return self.queue == []

    def queue_size(self):
        return len(self.queue)

if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    print(queue.dequeue())
    print(queue.peek())
    print(queue.queue_size())
    
