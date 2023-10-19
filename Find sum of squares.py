#sum of square
a=int(input("Enter an number: "))
sum=0
while(a>0):
    s=a%10
    a=a//10
    n=s**2
    sum=sum+n
print(sum)