    #ASKING FOR THE SIZE OF THE SACK
size=int(input("enter the size of the sack:"))

    #ASKING FOR THE WEIGHTS OF ALL OBJECTS SEPARTED BY SPACE
weights=input("\nENTER ALL THE WEIGHTS OF OBJECTS:")
weights=weights.split()

    #CONVERTING THE LIST ITEM FORM STRING TO INT
weights=[int(x) for x in weights]
print(f"weight val:{weights}\n")

    #ASKING FOR THE PROFIT FROM ALL THE OBJECTS SEPARTED BY SPACE
profits=input("\nENTER ALL THE PROFITS FROM THE OBJECTS (*RESPECTIVELY*):")
profits=profits.split()

    #CONVERTING THE LIST ITEM FORM STRING TO INT
profits=[int(y) for y in profits]
print(f"profits:{profits}\n")

    #MAKING A LIST OF THE TUPLES CONTAINING WEIGHTS AND PROFITS
arr=[(weights[i], profits[i]) for i in range(len(profits))]

    #SORTING THE ABOVE LIST IN DESCENDING ORDER OF PROFIT
sorted_arr=sorted(arr,key=lambda any: any[1],reverse=True)
print(f"sorted arr:{sorted_arr}")

    #DEFINING THE KNAPSACK FUNTION
def knapsack(sack_size, s_arr):

    #ASSIGNING THE FINAL ELEMENT TO RETURN TOTAL profit
    total_profit=0
    for item in s_arr:
        #IF NO SPACE LEFT IN SACK FOR ITEM BREAK THE CODE
        if item[0]>sack_size:
            break

        #ELSE SPACE IS THERE PUT THE ITEM AND 
        #INCREASE THE PROFIT OF THAT ITEM
        total_profit+=item[1]
        #DECRESE THE REMAINING SIZE OF THE SACK
        sack_size-=item[0]
    #FINALLY RETRUN THE PROFIT
    return total_profit

ans=knapsack(size,sorted_arr)
print(ans)