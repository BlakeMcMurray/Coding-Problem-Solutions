#finds the largest sum of a continuous sub array in array.
#Input: Array if positive and negative ints 
#output: Largest sum of subarray

def positive_sum(arr):
    best_sum = 0
    for i in range(len(arr)):
        sum_ = 0
        for j in range(i, len(arr)):
            sum_ += arr[j]
            if(sum_ > best_sum):
                best_sum = sum_
    return(best_sum)

def positive_sum_linear(arr):
    sum_ = 0
    best_sum = 0
    for i in arr:
        sum_ = sum_ + i
        if(sum_ < 0):
            sum_ = 0
        else:
            if(best_sum < sum_):
                best_sum = sum_
    return(best_sum)



print(positive_sum([2,-8,3,-2,4,-10]))
print(positive_sum_linear([2,-8,3,-2,4,-10]))
