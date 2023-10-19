#break
i=1
sum=0
while (i<=10):
    n=int(input("Enter number: "))
    if(n<0):
        print("Entered number is negative")
        break
    else:
        sum=sum+n
        i=i+1
    print(sum)