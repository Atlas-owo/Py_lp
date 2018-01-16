import math

print('Input a,b,c in order to get the anwser.')

a = input()
b = input()
c = input()

a = float(a)
b = float(b)
c = float(c)

if (b*b-4*a*c) < 0:
	print('This equation has no anwser.')
else:
	x = (-b+math.sqrt(b*b-4*a*c))/(2*a)
	y = (-b-math.sqrt(b*b-4*a*c))/(2*a)
	print('x1=',x,'\nx2=',y)