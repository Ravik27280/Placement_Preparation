# https://www.youtube.com/watch?v=cWvruDR-hJA

def SelectionSort(arr):
    sort=[]
    for i in range(len(arr)):
        a=min(arr)
        sort.append(a)
        arr.remove(a)
    return sort

array=[2,5,7,6,1,8,9,2]
print(SelectionSort(array))