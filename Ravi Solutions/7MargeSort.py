# https://www.youtube.com/watch?v=_trEkEX_-2Q&t=5s

def MargeSort(Arr):
    if len(Arr)>1:
        mid=len(Arr)//2
        left_Arr=Arr[:mid]
        Right_Arr=Arr[mid:]
        MargeSort(left_Arr)
        MargeSort(Right_Arr)
        i=0
        j=0
        k=0
        while i<len(left_Arr) and j<len(Right_Arr):
            if left_Arr[i]<Right_Arr[j]:
                Arr[k]=left_Arr[i]
                i=i+1
                k=k+1
            else:
                Arr[k]=Right_Arr[j]
                j=j+1
                k=k+1
        while i<len(left_Arr):
            Arr[k]=left_Arr[i]
            i=i+1
            k=k+1
        while j<len(Right_Arr):
            Arr[k]=Right_Arr[j]
            j=j+1
            k=k+1
    return Arr
array=[5,4,8,3,9,7,1]
print(MargeSort(array))
