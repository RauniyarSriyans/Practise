# stack implementation 

class Stack:

    def __init__(self):
        self.stack = []
        self.__maxstack = []

    def push(self, data):
        self.stack.append(data)
        
        if len(self.stack) == 1:
            self.__maxstack.append(data)
            return

        if data > self.__maxstack[-1]:
            self.__maxstack.append(data)
        else:
            self.__maxstack.append(self.__maxstack[-1])
    
    def pop(self):
        # don't do anything if the stack is empty
        if self.stack_size() < 1:
            return 
    
        data = self.stack[-1]
        del self.stack[-1]
        del self.__maxstack[-1]
        return data
    
    def peek(self):
        return self.stack[-1]
    
    def is_empty(self):
        return self.stack == []

    def stack_size(self):
        return len(self.stack)
    
    def stack_getmax(self):
        return self.__maxstack[-1]

if __name__ == '__main__':
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    print(stack.stack_size())
    print(stack.stack_getmax())
    print(stack.pop())
    print(stack.peek())
    print(stack.stack_size())
    print()
    print(stack.stack_getmax())
    print(stack.pop())
    print()
    print(stack.stack_getmax())
