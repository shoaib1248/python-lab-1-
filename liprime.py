print("enter the list to find prime number:")
l=[]
n=int(input("enter the size of the list:"))
for i in range (1,n+1):
    print("enter ",i," elemnt")
    ele=int(input())
    l.append(ele)
print(l)
for i in range(0,n):
    m=l[i]
    j=1
    count=0
    while j<m:
        if m%j==0:
            count+=1
        j+=1
    if count==1:
        print(l[i]," prime number")
    else:
        print(l[i]," not a prime number")