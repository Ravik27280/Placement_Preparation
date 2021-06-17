
def BinarySearch(A,Number):
    mid=len(A)//2
    if True:
        if A[mid]>=Number:
            for i in range(mid):
                if A[i]==Number:
                    return f"The place of",A[i],"is",i+1
                        
        else:
            for i in range(mid,len(A)):
                if A[i]==Number:
                    return f"The place of",A[i],"is",i+1

    return "Not found"

Arr=[1,3,6,8,9,11,15,19]
Num=int(input("Which No. You wnat to search = "))
print(BinarySearch(Arr,Num))