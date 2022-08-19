#DEFINING THE SEARCH FUNCTION
#MYLIST WILL BE SORTED LIST OR ARRAY
#KEY IS THE NUMBER TO FIND IN THE SORTED LIST
def Search(myList, key):
#ASSIGNING THE LOAWER BOUND AND UPPER BOUND
    low=1
    high=len(myList)
#RETURNING -1 IF THE NUMBER IS NOT FOUND
    if high<low:
        return -1
#RETURNING THE NUMBER IF FOUND
    else:
        mid= (high+low)//2
#IF THE NO. IS IN THE MID RETURN THE INDEX
        if myList[mid]==key:
            return mid
#IF NO. IS IN LEFT OR SMALLER RECURSION TO THE LIST FROM INDEX 0 TO MID-1
        elif key<myList[mid]:
            high=mid-1
            return Search(myList, key)
#IF NO. IS IN RHIGH OR BIGGER RECURSION TO THE LIST FROM INDEX MID+1 TO LAST INDEX
        elif myList[mid]<key:
            low=mid+1
            return Search(myList, key)

#STORING THE RESULT OF FUNCTION IN THE RESULT VAR
result=Search([12,34,56,78,90], 78)

#IF NUM FOUND/NOT FOUND THEN PRINTING THE INFO FOR USER UNDERSTANDING
if result == -1:
    print('the element is not present in the listt.')
else:
    print('element is present in the in the list at index' ,result)
