#fibonacci
n1=int(input("Enter a number: "))
n2=0
n3=1
count=0
if n1<=0:
    print("Enter a valid number")
elif n1==1:
    print("The series is",n1)
    print(n2)
else:
    print("The series is")
while count<n1:
    print(n2)
    x=n2+n3
    n2=n3
    n3=x
    count=count+1