#factorial
num=int(input("Enter a number\n"))
fact=1
while(num>1):
    fact=num*fact
    num=num-1
print("The factorial is",fact)