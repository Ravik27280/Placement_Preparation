# https://www.youtube.com/watch?v=kFeXwkgnQ9U

def Quicksort(Sequnace):
    length=len(Sequnace)
    if length<=1:
        return Sequnace
    else:
        pivot=Sequnace.pop()
    item_Greater=[]
    item_Lower=[]

    for item in Sequnace:
        if item>pivot:
            item_Greater.append(item)
        else:
            item_Lower.append(item)
    return Quicksort(item_Lower) + [pivot] + Quicksort(item_Greater)
print(Quicksort([10,8,9,5,7,1]))    



#Help of geeksfor geeks

# def partition(Start,End,Arr):
#     poivit_index=Start
#     poivit=Arr[poivit_index]
#     while Start<End:
#         while Start<len(Arr) and Arr[Start]<=poivit:
#             Start+=1
#         while Arr[End]>poivit:
#             End-=1
#         if Start<End:
#             Arr[Start],Arr[End]=Arr[End],Arr[Start]
#     Arr[End],Arr[poivit_index]=Arr[poivit_index],Arr[End]
#     return End
# def QuickShort(Start,End,Arr):
#     if Start<End:
#         p=partition(Start,End,Arr)
#         QuickShort(Start,p-1,Arr)
#         QuickShort(p+1,End,Arr)

# Arr=[10,7,8,9,1,5]
# QuickShort(0,len(Arr)-1,Arr)
# print(Arr)
