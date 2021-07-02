def Negative(Arr):
    Neg=[]
    pos=[]
# divide an array in two part positve and negative
    for i in range(len(Arr)):
        if Arr[i]<0:
            Neg.append(Arr[i])
        else:
            pos.append(Arr[i])
# For sort an array    
    Neg.sort()
    pos.sort()
    return (Neg+pos)

A=[1,5,-8,-6,-3,5,9,-7]
print(Negative(A))