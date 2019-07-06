#if an element in an m x n matrix is 0, it's entire
#row and column are set to zero

#O(m*n) solution: loops through matrix twice,
#first time to find the rows and columns with zeros
#in them, and second time to assign each value in those
#rows cols to zero
def zero_matrix(m):
    row = {}
    col = {}
    for i in range(len(m)):
        for j in range(len(m[0])):
            if(m[i][j] == 0):
                if(i not in row):
                    row[i] = 1
                if(j not in col):
                    col[j] = 1
    
    #set all vals in row to zero
    for i in row:
        for j in range(len(m[0])):
            m[i][j] = 0
    
    #set all vals in col to zero
    for j in col:
        for i in range(len(m)):
            m[i][j] = 0
    
    return(m)

m = [[1,0,1,1],[1,1,1,1],[0,1,1,0],[1,1,1,1]]
print(zero_matrix(m))
