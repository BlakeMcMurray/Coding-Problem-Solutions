import stack
class MyQueue:
    def __init__(self):
        self.s1 = stack.Stack()
        self.s2 = stack.Stack()
        self.nElems = 0

    def push(self, value):
        self.s1.push(value)
        self.nElems += 1
    
    def pop(self):
        if(self.s2.isEmpty()):
            while(self.s1.isEmpty() == False):
                self.s2.push(self.s1.pop().value)
            self.nElems -= 1
            return(self.s2.pop())
        else:
            self.nElems -= 1
            return(self.s2.pop())


queue = MyQueue()
queue.push(30)
queue.push(18)
print(queue.pop().value)
print(queue.pop().value)
