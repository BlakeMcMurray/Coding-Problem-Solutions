#given a string find the length of
#the longest substring without
#repeating chars.

#O(n) solution with 2 pointers
def longest_substring(s):
    p_1 = 0
    p_2 = 0
    max_count = 0
    letter_count = {}
    while(p_2 != len(s)):
        if s[p_2] not in letter_count:
            letter_count[s[p_2]] = 1
            p_2 += 1
        else:
            del letter_count[s[p_1]]
            p_1 += 1
        if(len(letter_count) > max_count):
            max_count = len(letter_count) 
        
        
    return(max_count)

print(longest_substring("mbsleodpwmm"))
