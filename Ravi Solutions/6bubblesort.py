#https://www.youtube.com/watch?v=g_xesqdQqvA

def bubbleSort(sequnce):
    Sroted=False
    while not Sroted:
        Sroted=True
        for item in range(len(sequnce)-1):
            if sequnce[item]>sequnce[item+1]:
                Sroted=False
                c=sequnce[item]
                sequnce[item]=sequnce[item+1]
                sequnce[item+1]=c
    return sequnce
print(bubbleSort([5,7,2,8,3,4]))

