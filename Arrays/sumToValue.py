#finds indexes of values that sum to val
#O(n) sol
def sum_to_value(val,arr):
    hash_t = {}
    pairs = []
    for i in arr:
        if i not in hash_t:
            hash_t[val - i] = i
        else:
            if (i,val-i) not in pairs:
                pairs.append((i,val-i))
    return(pairs)

print(sum_to_value(5,[2,-8,3,-2,4,-10,1,4]))

