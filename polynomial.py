n=int(input("enter the degree of the polynomial:"))
x=int(input("enter the value of the x:"))
i=n
val=0
while i>0:
     c=int(input("enter the coefficient of x^%d:"%i))   
     val+=c*(x**i)
     i-=1
c=int(input("enter the constant:"))
val+=c
print(val)