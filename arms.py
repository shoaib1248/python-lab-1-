n=int(input("enter a number to check whether it is armstrong or not:"))
a=n
b=n
p=0
sum=0
while a>0:
    r=a%10
    p+=1
    a=a//10
while b>0:
    r=b%10
    sum+=r**p
    b=b//10
if sum==n:
    print(n," is an armstrong number")
else:
    print(n," is not an armstrong number")