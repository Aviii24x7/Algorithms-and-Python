#LIST TO BE MERGED 

from turtle import right


my_list= [1,54,23,56,9,23,98,45,48] 


#HELPING FUNCTION TO MERGE TWO SORTED ARRAYS
def merge(left,right):

    merged_list=[]
    
    i=0     #LEFT ARRAY INDEX
    j=0     #RIGHT ARRAY INDEX

#KEEP DOING THE MERGING UNTIL THE list A or list B ITEMS GET FINISHED
    while i< len(left) and j<len(right):
        if left[i]>right[j]:

            merged_list.append(right[j])
            j+=1        #ALREADY ADD THE INDEX VALUE SO MOVING O THE NEXT

        else:
            merged_list.append(left[i])
            i+=1        #ALREADY ADD THE INDEX VALUE SO MOVING O THE NEXT

#ADDING THE ELEMENTS THAT MIGHT BE LEFT TO APPEND IF THE SIZE OF BOTH ARRAYS OR LIST ARE NOT SAME
    merged_list+= left[i:]
    merged_list+= right[j:]

#FINALLY THE FUNCTION WILL RETURN THE SOTED MERGED LIST
    return merged_list

#THE MAIN FUNCTION 
def merge_sort(arr):

#IF THE ARRAY IS EMPTY OR CONTAINS ONLY 1 ELEMENT IT IS SORTED ALREADY
    if len(arr)<=1:
        return arr

#FOR MULTIPLE ELEMENTS

    mid=len(arr)//2
    left = merge_sort(arr[:mid])    #assigning the left divided array
    right= merge_sort(arr[mid:])

    return merge(left,right)    #KEEP RETURNING THE MERGED SORTED ARRAY OF BOTH LEFT AND RIGHT ARR

x=merge_sort(my_list)
print(x)