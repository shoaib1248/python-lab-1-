print("enter the list to find armstrong number:")
l=[]
n=int(input("enter the size of the list:"))
for i in range (1,n+1):
    print("enter ",i," elemnt")
    ele=int(input())
    l.append(ele)
print(l)
for i in range(0,n):
    a=l[i]
    b=l[i]
    m=l[i]
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
    if sum==m:
       print(m," is an armstrong number")
    else:
       print(m," is not an armstrong number")