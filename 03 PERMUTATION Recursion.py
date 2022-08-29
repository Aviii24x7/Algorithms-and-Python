#function to return all permuations of string of length 3 
def permutations(mystr):
#Sorting the string for lexographical order
    mystr= sorted(mystr)
    if len(mystr) == 1:  
        return mystr
 
#recurssive call 
    perms = permutations(mystr[1:])  
#first letter  
    char = mystr[0] 
    result=[] 
 
    for perm in perms: 
        for i in range(len(perm) +1): 
#keeps the char in all the possible positions 
            result.append(perm[:i] + char + perm[i:]) 
    return result 

    
print(permutations('sat'))