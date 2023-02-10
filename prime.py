n=int(input("Enter a number to check whether it prime or not:"))
i=1
count=0
while i<n:
    if n%i==0:
        count+=1
    i+=1
if count==1:
    print("prime number")
else:
    print("not a prime number")