#print odd number from 1 to n
n=int(input("Enter the number:\t"))
i=0
while(i<=n):
    if(i%2==0):
        print("\t")
        i+=1
    else:
        print(i)
        i+=1