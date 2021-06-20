import sys


def MinArray(A):
    mi=sys.maxsize
    for i in range(len(A)):
        if mi>A[i]:
            mi=A[i]
        else:
            pass
    return mi

arr=[5,2,77,1,8,5]
print(MinArray(arr))