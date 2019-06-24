import singleLinkList as sll 
class Stack:
    def __init__(self):
        self.ll = sll.SinglyLinkedList()
        self.height = 0

    #pops the last inputed element to the stack
    def pop(self):
        if(self.isEmpty()):
            print("The stack is empty")
        else:
            n = self.ll.removeFromFront()
            self.height -= 1
            return(n)


    def push(self,item):
        self.ll.addToFront(item)
        self.height += 1

    def peek(self):
        if(self.ll.head.next):
            return(self.ll.head.next.value)
        else:
            print("The Stack is empty")

    def isEmpty(self):
        if(self.height == 0):
            return(True)
        return(False)

    #Sorts a stack
    def stackSort(self):
        temp = Stack()
        temp.push(self.pop().value)
        while(self.isEmpty() != True):
            if(self.peek() >= temp.peek()):
                temp.push(self.pop().value)
            else:
                minNode = self.pop()
                while(temp.peek() > minNode.value or temp.isEmpty()):
                    self.push(temp.pop().value)
                temp.push(minNode.value)
        temp.ll.printList()
        while(temp.isEmpty() == False):
            self.push(temp.pop().value)
    
s = Stack()
s.push(4)
s.push(2)
s.push(8)
s.push(9)
s.push(1)
s.stackSort()
s.ll.printList()





