#method to compute all permutations of a string
def swap(s, i, j):
    copy = s[i]
    s[i] = s[j]
    s[j] = copy
    return(s)


def compute_permutations(s,permutations,count):
    
    if(count == s - 1):
        return(permutations)
    m = len(permutations)
    for i in range(0,m):
        curr = list(permutations[i])
        for j in range(count+1,s):
            permutations.append(''.join(swap(curr,count,j)))
    return(compute_permutations(s,permutations,count+1))

def permute(string_s):

    permutations = [string_s]
    count = 0
    s = len(string_s)
    perms = compute_permutations(s,permutations,count)
    perms = list(set(perms))
    return(perms)

print(permute('abc'))


