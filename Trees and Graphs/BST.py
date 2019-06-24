from collections import deque
class BST:
    def __init__(self,value):
        self.value = value
        self.lChild = None
        self.rChild = None
        self.parent = None
    
    def insert(self,value):
        curr = self
        while(curr):
            if(curr.value == value):
                print("value already in tree")
                break
            if(curr.value > value and curr.lChild):
                curr = curr.lChild
                continue
            if(curr.value > value and curr.lChild == None):
                curr.lChild = BST(value)
                break
            if(curr.value < value and curr.rChild):
                curr = curr.rChild
                continue
            if(curr.value < value and curr.rChild == None):
                curr.rChild = BST(value)
                break      
    #working
    def BFS(self):
        queue = deque([])
        curr = self
        queue.append(curr)
        while(len(queue) != 0):
            curr = queue.popleft()
            print(curr.value)
            if(curr.lChild):
                queue.append(curr.lChild)
            if(curr.rChild):
                queue.append(curr.rChild)

#working
def DFS(bst):
    if(bst == None):
        return()
    print(bst.value)
    DFS(bst.lChild)
    DFS(bst.rChild)

#4.4 in Cracking Coding-----
def is_balanced_recursive(bst):
    if(bst == None):
        return(True,-1)
    hL = is_balanced_recursive(bst.lChild)
    hR = is_balanced_recursive(bst.rChild)
    if((abs(hL[1] - hR[1]) <= 1) and hL[0] == True and hR[0] == True):
        return(True,max(hL[1]+1,hR[1]+1))
    else:
        return(False,-1)

def is_balanced(bst):
    return(is_balanced_recursive(bst)[0])
#---------------------------
#4.5 in Cracking coding-----
def validate_bst(bst):
    queue = deque([])
    curr = bst
    queue.append(curr)
    while(len(queue) != 0):
        curr = queue.popleft()
        if(curr.lChild):
            if(curr.lChild.value < curr.value):
                queue.append(curr.lChild)
            else:
                return(False)
        if(curr.rChild):
            if(curr.rChild.value > curr.value):
                queue.append(curr.rChild)
            else:
                return(False)
    return(True)
#---------------------------

#4.6 in Cracking coding-----
def is_right_child(node):
    try:
        flag = (node.parent.rChild == node)
    except:
        return(False)

    return(flag)

def is_left_child(node):
    try:
        flag = (node.parent.lChild == node)
    except:
        return(False) 
    return(flag)

def successor(node):
    if(node.rChild):
        node = node.rChild
        while(node.lChild):
            node = node.lChild
        return(node)
    else:
        while(is_right_child(node)):
            node = node.parent
        if(node.parent == None):
            return("No in order Successor")
        else:
            return(node.parent) 
#---------------------------

    

bst = BST(5)
bst.insert(3)
bst.insert(2)
bst.insert(6)
bst.insert(4)



bst.BFS()
print(is_balanced(bst))
print(validate_bst(bst))
        

