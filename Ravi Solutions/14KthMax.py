def KMax(Arr,n):
    for i in range(n-1):
        Arr.remove(max(Arr))
    return max(Arr)

a=[5,7,8,2,9,1]
print (KMax(a,1))