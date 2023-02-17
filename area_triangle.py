print("enter the sides of the triangle:")
a=int(input("side 1:"))
b=int(input("side 2:"))
c=int(input("side 3:"))
import math
s=(a+b+c)/2
area=math.sqrt(s*(s-a)*(s-b)*(s-c))
print("area:",area)