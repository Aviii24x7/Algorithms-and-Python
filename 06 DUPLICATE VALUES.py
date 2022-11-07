def Duplicate(mylist):

#A SET TO STORE THE NON-DUPLICATE VALUES
    mySet=set()
#A SET TO STORE THE DUPLICATE VALUES
    dupli=set()
#LOOP GOING TO EVERY VALUE IN MYLIST AND ADDING DUPLICATES IN DUPLI SET
    for i in mylist:

        if i not in mySet:
            mySet.add(i)
        elif i in mySet:
            dupli.add(i)
    return dupli

print(Duplicate([1,2,3,4,1,3,"a","a"]))