def ecfc(a,b,c):
    import math
    d = b*b-4*a*c
    if d<0:
        return 'No answer'
    else:
        x1 = (-b + math.sqrt(d))/(2*a)
        x2 = (-b - math.sqrt(d))/(2*a)
        return x1,x2

print('For 1,3,-4  the answer is' , ecfc(1,3,-4))
