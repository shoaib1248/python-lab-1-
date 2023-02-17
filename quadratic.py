a=int(input("enter the coefficient of x^2:"))
b=int(input("enter the coefficient of x:"))
c=int(input("enter the constant value:"))
import math
d=math.sqrt(b**2-4*a*c)
if d>=0:
    r1=(-b+d)/2*a
    r2=(-b-d)/2*a
    print("root1:",r1)
    print("root2:",r2)