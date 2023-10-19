#Divisiblity test by 7
n=int(input("Enter a number between 100 to 200: "))

if(n>=100 and n<=200):
    if(n%7==0):
        print("Divisible by 7")
    else:
        print("Not divisible by 7")
else:
    print("Enter a number which is between 100 to 200")