def RS(Arr):
    rev=[]
    for i in range(len(Arr)-1,-1,-1):
        rev.append(Arr[i])
    return rev
Arr=[1,2,3,4,5,6]
print(RS(Arr))