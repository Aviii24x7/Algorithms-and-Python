#FUNCTION TO CHECK IF THE STRING IS PALINDROME OR NOT
def check_palindrome(my_str):
    if my_str==my_str[::-1]:
        return True
    else:
        return False

#FUNCTION THAT GIVES FINAL INDEX LIST
def cutout_string(my_string,i_index):
    f_index_list = []
    for f_index in range(i_index+1,len(my_string)):
        if my_string[i_index] == my_string[f_index]:
            f_index_list.append(f_index)
    return f_index_list

#PARENT STRING
name= 'AVIVAAPQSQPAAVIVA'

#LIST OF ALL THE FINAL INDEX
end_list=cutout_string(name,0)

slice_str=[]
#APPENDING THE CUTOUT STRING WHICH HAVE SAME ALPHABET AS INDEX 0 IN SLICE_STR LIST
for f in end_list:
    slice_str.append(name[0:f+1])

#CHECKING IF THE CUTOUT STRINGS ARE PALINDROME
for st in slice_str:
    if check_palindrome(st):
        print(st)
