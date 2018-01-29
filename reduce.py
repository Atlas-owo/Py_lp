from functools import reduce

def prod(L):
    return reduce(a,L)

def a(x,y):
    return x*y

print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
