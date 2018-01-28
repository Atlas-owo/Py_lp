def tri():
    yield [1]
    
    a = [1,1]

    while(True):
        yield a
        for x in range(len(a)-1):
            a[x] = a[x] + a[x+1]
        a.insert(0,1)
        
        

t = tri()
i = 0
while(i < 20):
    print(next(t))
    i+=1
