#recursive function to find the nth term in the fibonacci series
def fibonacci(n):
    if(n == 0):
        return(0)
    if(n == 1):
        return(1)
    return(fibonacci(n-1)+fibonacci(n-2))

#dynamic prog solution to fibonacci
def dynFib(n):
    arr = n*[1]
    for i in range(2,n):
        arr[i] = arr[i-1]+ arr[i-2]
    return(arr[n-1])

print(fibonacci(7))
print(dynFib(7))
