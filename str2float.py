from functools import reduce

def fn(m,n):
    return (10 * m) + n

def fm(m,n):
    return (m / 10) + n

d = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}

def char2int(c):
    return d[c]

def str2float(s):
    for i in range(len(s)):
        if s[i] == '/':
            a = s[0:i]
            b = s[i+1:len(s)]
            break
        '''
        a = reduce(fn,map(char2int,s1))
        s2 = map(char2int,s2)
        s2.reverse()
        b = reduce(fm,s2)
        return a + b
        '''
    print(a,b)
    c = reduce(fn,map(char2int,a))
    print(c)

    d = (reduce(fn,map(char2int,b)))*(10**(-len(b)))
    print(d)

    return c + d

print('3453/6543 is changed into',str2float('3453/6543'))
