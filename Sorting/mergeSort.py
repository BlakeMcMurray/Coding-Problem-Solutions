#working
import math
def merge(l1,l2):
    sort_L = []
    c1 = 0
    c2 = 0
    while(c1 != len(l1) and c2 != len(l2)):
        if l1[c1] <= l2[c2]:
            sort_L.append(l1[c1])
            c1 += 1
        else:
            sort_L.append(l2[c2])
            c2 += 1
    if(c1 != len(l1)):
        for i in range(c1,len(l1)):
            sort_L.append(l1[i])
    if(c2 != len(l2)):
        for i in range(c2,len(l2)):
            sort_L.append(l2[i])
    return(sort_L)


def merge_sort(list_):
    if(len(list_) == 1):
        return(list_)   
    l1 = merge_sort(list_[:(len(list_)//2)])
    l2 = merge_sort(list_[(len(list_)//2):])
    return(merge(l1,l2))

    
    


print(merge_sort([3,893,29,25,69,5,0]))