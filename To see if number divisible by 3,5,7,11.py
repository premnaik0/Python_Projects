#To see if number is divisible by 3,5,7,11
n=int(input("Enter a number:\t"))

if(n%3==0):
    print("The number is divisible by 3")
elif(n%5==0):
    print("The number is divisible by 5")
elif(n%7==0):
    print("The number is divisible by 7")
elif(n%11==0):
    print("The number is divisible by 11")
else:
    print("The following number is not divisible by 3,5,7,11")