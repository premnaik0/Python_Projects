#calculator
 
choise=int(input("Press 1 for Addition\nPress 2 for Subtraction\nPress 3 for Multiplication\nPress 4 for Division\n"))

if(choise==1):
    a=int(input("Enter 1 number: "))
    b=int(input("Enter 2 number: "))
    c=a+b
    print("the sum is",c)
elif(choise==2):
    a=int(input("Enter 1 number: "))
    b=int(input("Enter 2 number: "))
    c=a-b
    print("the ans is",c)
elif(choise==3):
    a=int(input("Enter 1 number: "))
    b=int(input("Enter 2 number: "))
    c=a*b
    print("the ans is",c)
elif(choise==4):
    a=int(input("Enter 1 number: "))
    b=int(input("Enter 2 number: "))
    c=a/b
    print("The answer is",c)
else:
    print("Choose a valid option")