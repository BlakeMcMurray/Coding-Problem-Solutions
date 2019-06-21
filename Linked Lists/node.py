#node class
class Node:
    def __init__(self):
        self.value = None
        self.next = None

    def gett(self):
        return(self.value)
    
    def sett(self,value):
        self.value = value

    def has_next(self):
        if(self.next != None):
            return(True)
        else:
            return(False)




