import math
def swap(i,j,arr):
    copy = arr[i]
    arr[i] = arr[j]
    arr[j] = copy
    return(arr)

def selection_sort(arr_):
    for i in range(len(arr_)):
        min_ = arr_[i]
        index = i
        for j in range(i,len(arr_)):
            if(min_ > arr_[j]):
                min_ = arr_[j]
                index = j
        arr_ = swap(i,index,arr_)
    return(arr_)

print(selection_sort([19,6,20,5,23,23,2,3]))
            
