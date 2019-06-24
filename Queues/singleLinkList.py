import node
class SinglyLinkedList:

    def __init__(self):
        self.head  = node.Node()
        self.length = 0
    
    def insert(self,value):
        n = node.Node()
        n.sett(value)
        copy = self.head
        while(copy.hasNext()):
            copy = copy.next 
        copy.next = n 
        self.length += 1

    def printList(self):
        copy = self.head
        copy = copy.next
        l = []
        while copy != None:
            l.append(copy.value)
            copy = copy.next
        print("list is: ",l)
    
    def insertMany(self,nums):
        copy = self.head
        while(copy.next != None):
            copy = copy.next
        for i in nums:
            n = node.Node()
            n.sett(i)
            copy.next = n
            copy = copy.next
            self.length += 1

    #deletes all nodes of the given value in sll
    def delete(self,value):
        prev = self.head
        copy = prev.next
        while prev.hasNext():  
            if copy.value == value:
                prev.next = copy.next
                copy = prev.next
                self.length -= 1
            else:
                prev = prev.next
                copy = prev.next
    #solution to remove duplicates using without temp buffer
    def removeDuplicates(self):
        r1 = self.head
        prev = r1
        r2 = r1.next
        if(r2 == None):
            return()
        r1 = r1.next
        r2 = r2.next
        prev = r1
        if r2 == None:
            return()
        while(r1.next != None):
            while(r2 != None):
                if(r1.value == r2.value):
                    prev.next = r2.next
                    r2 = r2.next
                else:
                    prev = r2
                    r2 = r2.next
            r1 = r1.next 
            prev = r1
            if(r1 == None):
                return()
            else:
                r2 = r1.next
    def findKthToLast(self,k):
        count = 0
        curr = self.head
        while curr.next != None:
            curr = curr.next
            count += 1
        curr = self.head
        nSteps = count - k + 1
        count = 0
        while(count != nSteps):
            curr = curr.next
            count += 1
        return(curr.value)
    
    #removes the first node in the ll and returns it
    def removeFromFront(self):
        if(self.head.next == None):
            return(None)

        n = self.head.next
        self.head.next = self.head.next.next
        return(n)
    
    
    def addToFront(self,val):
        n = node.Node()
        n.sett(val)
        n.next = self.head.next
        self.head.next = n


         


        

    
    










    
    


        
            

        

    


