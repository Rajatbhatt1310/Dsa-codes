class Node:
    def __init__(self,value=None,next=None):
        self.value = value
        self.next = None

class Stack :
    def __init__(self):
        self.start = None
        self.count = 0

    def is_empty(self):
        temp = self.start
        if temp is None:
            return "Empty"
        

    def push(self,stack_data):
        new_node = Node(stack_data,self.start)
        self.start = new_node
        return
    
    def pop(self):
        temp = self.start
        while temp is not None:
            temp = temp.next
            if temp==None:
                temp.pop()
            self.count-=1    
            return
    def peek(self):

            
    

                
        



  


        