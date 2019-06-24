from collections import deque
class BinaryTreeNode:
    def __init__(self,value):
        self.value = value
        self.lChild = None
        self.rChild = None
    
    def insert(self,value):
        queue = deque([])
        curr = self
        queue.append(curr)
        while(len(queue) != 0):
            curr = queue.popleft()
            if(curr.lChild == None):
                curr.lChild = BinaryTreeNode(value)
                break
            else:
                queue.append(curr.lChild)
            if(curr.rChild == None):
                curr.rChild = BinaryTreeNode(value)
                break
            else:
                queue.append(curr.rChild)

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

#validates whether tree is a binary search tree
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


binTree = BinaryTreeNode(0)
binTree.insert(1)
binTree.insert(2)
binTree.insert(3)
binTree.insert(4)
binTree.insert(5)
binTree.insert(6)
binTree.insert(4)

binTree.BFS()
print(validate_bst(binTree))


        

        
