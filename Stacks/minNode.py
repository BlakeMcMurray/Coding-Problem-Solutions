class MinNode:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.min = None

    def gett(self):
        return(self.value)
    
    def sett(self,value):
        self.value = value

    def hasNext(self):
        if(self.next != None):
            return(True)
        else:
            return(False)




