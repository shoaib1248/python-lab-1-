print("enter up to which you want to print fibbonecy series:")
n=int(input("n="))
print(0)
x=0
y=1
count=1
while count<=n-1:
    count+=1
    print(y)
    sum=x+y
    x=y
    y=sum