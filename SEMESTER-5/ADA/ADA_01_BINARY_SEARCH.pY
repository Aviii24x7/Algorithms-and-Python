def Search(myList, key):
    low=1
    high=len(myList)

    if high<low:
        return -1
    else:
        mid= (high+low)//2

        if myList[mid]==key:
            return mid

        elif key<myList[mid]:
            high=mid-1
            return Search(myList, key)

        elif myList[mid]<key:
            low=mid+1
            return Search(myList, key)

result=Search([12,34,56,78,90], 78)
if result == -1:
    print('the element is not present in the listt.')
else:
    print('element is present in the in the list at index' ,result)
