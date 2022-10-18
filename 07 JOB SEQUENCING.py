
def job_sequence(tuples, max_deadline):
    '''a function to implement job sequencing problem'''
    '''sorting the passed array 
    on the basis of their deadlines'''
    arr = sorted(tuples, key=lambda y: y[2], reverse=True)
    j_exe = []    # an empty list to collect results
    max_profit = 0

    for a in range(len(arr)-1):  # logic to get maximum item for 2 same deadlines
        if arr[a][2] == arr[a+1][2]:
            max_item = arr[a]
            break
        else:
            max_item = ("", 0, 0)

    for i in range(max_deadline):  # to create a slot equal to the max deadlines
        max_item = (max_item[0], 0, 0)
        for item in arr:  # iterating list.
            if item[2] == i+1:
                if item[1] > max_item[1]:
                    # assigning the max item after it satisfies the job sequencing conditions.
                    max_item = item
        j_exe.append(max_item)  # appending the result

    return [i for i in j_exe]   # return list of jobs.


# Main code
print("Enter the jobs")
jobs = [str(i) for i in input().split()]
print("Enter the Deadlines")
deadlines = [int(i) for i in input().split()]
print("Enter the profits")
profits = [int(i) for i in input().split()]


tuples = [(jobs[i], profits[i], deadlines[i]) for i in range(0, len(jobs))]
print(job_sequence(tuples, max(deadlines)))
