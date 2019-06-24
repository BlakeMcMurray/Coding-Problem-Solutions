import math
def getParent(index):
    if(index == 0):
        print("Root has no parent")
        return(None)
    else:
        return(index - math.floor(index/2) - 1) 

class Heap:
    def __init__(self,value):
        self.tree = [value]
        self.nElems = 1
    
    def insert(self,value):
        self.tree.append(value)
        self.nElems += 1
        index = len(self.tree) - 1
        while(self.tree[index] < self.tree[getParent(index)]):
            copy = self.tree[index]
            self.tree[index] = self.tree[getParent(index)]
            self.tree[getParent(index)] = copy
            index = getParent(index)
            if(index == 0):
                return()
        

    def deleteMin(self):
        min_V = self.Tree[0]
        
        return(min_V)
            

        

h = Heap(3)
h.insert(4)
h.insert(7)
h.insert(5)
h.insert(6)
h.insert(8)
h.insert(10)
h.insert(8)
h.insert(2)
h.insert(5)
print(h.tree)
    

    
