#Reversing a number
n=int(input("Enter a number:\t"))
sum=0
while(n>0):
    s=n%10
    sum=(sum*10)+s
    n=n//10
print("The revered number is:",sum)