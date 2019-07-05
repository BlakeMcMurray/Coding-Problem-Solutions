#code to tell if 2 strings are anagrams
#hashtable sol: O(n + m) where n and m are the lengths 
#of the 2 strings
def anagram(s_1, s_2):
    if(len(s_1) != len(s_2)):
        return(False)
    letter_count_1 = {}
    letter_count_2 = {}
    for i in s_1:
        if(i in letter_count_1):
            letter_count_1[i] += 1
        else:
            letter_count_1[i] = 1
    for i in s_2:
        if(i in letter_count_1 and i not in letter_count_2):
            letter_count_2[i] = 1
        elif(i in letter_count_1 and i in letter_count_2 and letter_count_1[i] > letter_count_2[i]):
            letter_count_2[i] += 1
        else:
            return(False)
    return(True)
         
        
#sorting solution: O(nlogn + mlogm)
def anagram_sort(s_1,s_2):
    if(len(s_1) != len(s_2)):
        return(False)
    
    s_1 = sorted(s_1)
    s_2 = sorted(s_2)
    for i in range(len(s_1)):
        if(s_1[i] != s_2[i]):
            return(False)
    return(True)

s_1 = "Hello"
s_2 = "eHlol"


print(anagram(s_1,s_2))
print(anagram_sort(s_1,s_2))



