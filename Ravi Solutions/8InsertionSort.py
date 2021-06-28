# https://www.youtube.com/watch?v=byHi41L9vTM&t=122s
def InsertionSort(Arr):
    for i in range(1,len(Arr)):
        while Arr[i-1]>Arr[i] and i>0:
            Arr[i-1],Arr[i]=Arr[i],Arr[i-1]
            i=i-1
    return Arr
print(InsertionSort([5,6,9,4,2]))
