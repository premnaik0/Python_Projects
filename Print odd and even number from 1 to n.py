#print odd and even number from 1 to n
n=int(input("Enter the number:\t"))
i=1
if(i<=n):
    print("Even numbers")
else:
    print("Odd numbers")
while(i<=n):
    if(i%2==0):
        print("\n",i)
        i+=1
    else:
        print("\t",i)
        i+=1