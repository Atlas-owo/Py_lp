import math

print('For equation ax^2+bx+c = 0 , input a,b,c in order to get the anwser.')

t=1

i=0
inp=['/']*3

while i<=2:
    inp[i] = input()
    inp[i] = float(inp[i])
    i+=1
    

a=inp[0]
b=inp[1]
c=inp[2]


if (b*b-4*a*c) < 0:
    print('This equation has no anwser.')
else:
    x = (-b+math.sqrt(b*b-4*a*c))/(2*a)
    y = (-b-math.sqrt(b*b-4*a*c))/(2*a)
    print('x1=%f\nx2=%f'%(x,y))
