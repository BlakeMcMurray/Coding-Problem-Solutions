#checks if string contains only unique chars
#without additional storage
#O(n^2) complexity
def two_pointer_uc(st):
    for i in range(len(st)):
        for j in range(i+1,len(st)):
            if st[i] == st[j]:
                return(False)
    return(True)

#O(nlogn) solution
def sort_uc(st):
    st = sorted(st)
    for i in range (1,len(st)):
        if(st[i-1] == st[i]):
            return(False)
    return(True)

print(two_pointer_uc("abdjekc"))
print(sort_uc("csamac"))