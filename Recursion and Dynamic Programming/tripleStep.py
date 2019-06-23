#recursive solution
def tripStep(n):
    if(n == 3):
        return(4)
    if(n == 2):
        return(2)
    if(n == 1):
        return(1)

    return(tripStep(n-1) + tripStep(n-2) + tripStep(n-3))

print(tripStep(6))

#dynamic programming solution
def dynamicTripStep(n):
    arr = n*[0]
    arr[0] = 1
    arr[1] = 2
    arr[2] = 4
    for i in range(3,n):
        arr[i] = arr[i-1] + arr[i-2] + arr[i-3]
    return(arr[n-1])

print(dynamicTripStep(6))