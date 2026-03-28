class Stack(list):
    
    def is_empty(self):
        if len(self)==0:
            return "empty list"
        else:
            return False

    def push(self,n):
        self.append(n)
        return Stack
    
    def pop(self):
        if len(self)==0:
            return None
        else:
            super().pop()
            return self
        
    def peek(self):
        if not self.is_empty():
            temp = self[-1]
            return temp
        else:
            return IndexError("Empty list")

    def size(self):
        length = len(self)
        return length
    
    def insert(self,index,n):
        raise self.AttributeError("No insert() method is ther in list")
        
my_s = Stack()
my_s.push(34)
my_s.push(54)        
my_s.push(9)        
my_s.push(67)

print(my_s.insert(4))     

    
