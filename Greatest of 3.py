#Greatest of 3

n1=int(input("Enter number1\n"))
n2=int(input("Enter number2\n"))
n3=int(input("Enter number3\n"))

if(n1==n2) and (n1==n3):
    print("All 3 numbers are same")
elif(n2>n1) and (n2>n3):
    print("number 2 is greater")
elif(n1>n2) and (n1>n3):
    print("number 1 is greater")
else:
    print("number 3 is greater")