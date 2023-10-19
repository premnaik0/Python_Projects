#age
a=0
s=0
b=0
i=1
while(i<=10):
    age=int(input("Enter age: "))
    if(age<=5):
        b+=1
    elif(age>18):
        a+=1
    elif(age<=18):
        s+=1
    else:
        print("Enter valid number")
    i+=1
print("Baby:",b)
print("Adult:",a)
print("School:",s)