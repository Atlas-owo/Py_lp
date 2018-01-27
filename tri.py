def tri():
    a = [1,2,1]

    while(True):
        yield a
        for x in range(len(a)-1):
            a[x] = a[x] + a[x+1]
        a.insert(0,1)
        
        

t = tri()
print(next(t))
print(next(t))
print(next(t))
