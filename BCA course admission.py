#BCA course admission

sum=0

m=int(input("Enter marks for math: "))
s=int(input("Enter marks for science: "))
e=int(input("Enter marks for english: "))

if(m>=40):
    print("Pass in math")
else:
    print("Fail in math")
    
if(s>=40):
    print("Pass in science")
else:
    print("Fail in science")
    
if(e>=40):
    print("Pass in english")
else:
    print("Fail in english")

sum=m+s+e

if(m>=40 and s>=40 and e>=40 and sum>=120):
    print("Welcome to BCA")
else:
    print("Thanks for appling try next time")