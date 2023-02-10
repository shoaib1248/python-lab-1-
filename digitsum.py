n=int(input("enter the number:"))
b=n
sum=0
while b>0:
    r=b%10
    sum+=r
    b=b//10
print(sum)