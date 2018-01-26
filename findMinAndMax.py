def findMinAndMax(L):
    if L == []:
        return (None,None)
    elif len(L) == 1:
        return (L[0],L[0])
    else:
        Max = L[0]
        Min = L[0]
        for x in range(len(L)):
            if L[x] < Min:
                Min = L[x]
            if L[x] > Max:
                Max = L[x]
        return (Min,Max)
    
print(findMinAndMax([4,6,4,2,6,7,3,1]))
