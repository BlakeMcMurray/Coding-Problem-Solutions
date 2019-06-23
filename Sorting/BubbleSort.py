def swap(i,j,arr):
    copy = arr[i]
    arr[i] = arr[j]
    arr[j] = copy
    return(arr)

def bubble_sort(arr):
    for j in reversed(range(len(arr))):
        for i in range(j):
            if(arr[i] > arr[i+1]):
                arr = swap(i,i+1,arr)
    return(arr)

print(bubble_sort([19,6,20,5,23,23,2,3]))