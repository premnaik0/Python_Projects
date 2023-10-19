#sum
i=1
sum=0
while(i<=10.):
    n=int(input("Enter number: "))
    if(n>0):
        sum=sum+n
        i+=1
    else:
        n=0
        print("Please enter positive number")
print("Sum of positive numbers:",sum)