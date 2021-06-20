import sys
def MaxArr(A):
    mi=-sys.maxsize
    for i in range (len(A)):
        if mi<A[i]:
            mi=A[i]
        else:
            pass
    return mi
arr=[10,5,88,12,7,6]
print(MaxArr(arr))