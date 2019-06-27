#reverse a C-Style String
import math
def swap(i,j,arr):
    copy = arr[i]
    arr[i] = arr[j]
    arr[j] = copy
    return(arr)

def rev_cs_string(ch_arr):
    for i in range(int(math.floor(len(ch_arr)/2))):
        ch_arr = swap(i,len(ch_arr)-2-i,ch_arr)
    return(ch_arr)

ch_arr = ['a','b','c','_']
print(rev_cs_string(ch_arr))
ch_arr = ['a','b','c','d','_']
print(rev_cs_string(ch_arr))