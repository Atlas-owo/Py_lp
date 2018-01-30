def fn(m,n):
    return (10 * m) + n

def fm(m,n):
    return (m / 10) + n

d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2int(c):
    return d[c]

def str2float(s):
    for i in s:
        if s[i] == '/':
            s1 = s[0:i-1]
            s2 = s[i+1:len(s)-1]
            break
        a = reduce(fn,map(char2int,s1))
        s2 = map(char2int,s2)
        s2.reverse()
        b = reduce(fm,s2)

        return a + b
print(str2float('34/6'))
