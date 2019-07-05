#algorithm to replace spaces in a string with '#$'
#O(n^2) solution (because of string copying)
def replace_spaces(s):
    s_new  = ""
    for i in s:
        if(i == ' '):
            s_new += "#$"
        else:
            s_new += i
    return(s_new)

#O(n) solution assuming C-style string or 'char' array
#note: python does not actually have char data type
def replace_spaces_c(s):
    s_num = 0
    for i in s:
        if i == " ":
            s_num += 1
  
    s_new = ['']*(len(s)+(s_num))
    count = 0
    for i in s:
        if i == " ": 
            s_new[count] = "#"
            count += 1
            s_new[count] = "$"
            count += 1
        else:
            s_new[count] = i
            count += 1

    return(''.join(s_new))
print(replace_spaces("Hello my friend"))
print(replace_spaces_c("Hello my friend"))