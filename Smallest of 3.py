#Smallest of 3
def smallest():
    n1=int(input("Enter N1: "))
    n2=int(input("Enter N2: "))
    n3=int(input("Enter N3: "))
    
    if(n1==0 and n2==0 and n3==0):
        print("All the numbers are zero")
    elif(n1==n2 and n1==n3):
        print("All numbers are equal")
    elif(n1<n2 and n1<n3):
        print("N1 is smallest",n1)
    elif(n2<n1 and n2<n3):
        print("N2 is smallest: ",n2)
    else:
        print("N3 is smallest: ",n3)
smallest()