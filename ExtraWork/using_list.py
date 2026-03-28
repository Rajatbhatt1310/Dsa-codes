class Stack:

    def __init__(self,):
        self.stck = []

    def is_empty(self):
        if len(self.stck) == 0:
            return "Empty stack"
        else:
            return "Not empty"

    def push(self,n):
        self.stck.append(n)
        return self.stck
    
    def pop(self):
        if len(self.stck) == 0:
            return "Its an empty stack. Not possible"
        else:        
            self.stck.pop()
        return self.stck

    def peek(self):
        if len(self.stck) == 0:
            return "Empty string"
        else:
            temp = self.stck[-1]
            return (temp)

    def size(self):
        size = len(self.stck)
        return size
        
s = Stack()
(s.push(34))
(s.push(100))
(s.push(53))
(s.pop())
print(s.peek())
print(s.size())




