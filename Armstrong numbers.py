#Armstrong numbers
n=int(input("Enter number: "))
num=0
c=0
x=n
while(n!=0):
    num=n%10
    c+=(num*num*num)
    n=n//10
if(c==x):
    print( "The following is a Armstrong number")
else:
    print("The following is not a Armstrong number")