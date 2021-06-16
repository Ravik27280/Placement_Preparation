def LenearSearch(n):
    if True:
        for i in range(len(Arr)):
            if Arr[i]==n:
                return f"Poestion of",Arr[i],"is = ",i
    return("No exist")

Arr=[1,10,6,5,8,11,7,9,14]
n=int(input("Enter a no you want to search="))
print(LenearSearch(n))
        
