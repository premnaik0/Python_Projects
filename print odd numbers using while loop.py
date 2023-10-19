#print odd numbers using while loop
i=int(input("Enter n value: "))
n=1
while(n<i):
    if(n%2==0):
        n+=1
    else:
        print(n)
        n+=1