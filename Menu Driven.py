#Menu driven
o=input("Enter operator:\t")
n1=int(input("Enter number1:\t"))
n2=int(input("Enter number2:\t"))

if(o=='+'):
    s=n1+n2
    print(s)
elif(o=='-'):
    s=n1-n2
    print(s)
elif(o=='*'):
    s=n1*n2
    print(s)
elif(o=='/'):
    s=n1/n2
    print(s)
elif(o=='**'):
    s=n1**n2
    print(s)
elif(o=='//'):
    s=n1//n2
    print(s)
else:
    print("Enter a valid operator")