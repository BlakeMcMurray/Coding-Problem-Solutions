import minNode as MN

#class to create a min stack. Minimum value in the stack
#is stored in the node 
class MinStack:
    def __init__(self):
        self.top = None
        self.elems = 0

    def push(self,elem):
        if(self.top == None):
            self.top = MN.MinNode(elem)
            self.top.min = elem
            
        else:
            node = MN.MinNode(elem)
            if(elem < self.top.min):
                node.min = elem
            else:
                node.min = self.top.min
            node.next = self.top
            self.top = node

        self.elems += 1
    
    def pop(self):
        if(self.top == None):
            return(None)

        node = self.top
        self.top = node.next
        self.elems -= 1
        return(node.value)

    def return_min(self):
        return(self.top.min)

min_stack = MinStack()
min_stack.push(14)
print(min_stack.return_min())
min_stack.push(12)
min_stack.push(18)
min_stack.push(11)
min_stack.push(15)
print(min_stack.return_min())
print(min_stack.pop())
print(min_stack.pop())
print("should return 12: ",min_stack.return_min())






        