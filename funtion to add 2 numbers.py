#Calculator 2.0
def main():
    c=int(input("Press 1 for Additon\nPress 2 for Subtraction\nPress 3 for Multiplication\nPress 4 for Division\n:"))

    if(c==1):
        sum()
    elif(c==2):
        sub()
    elif(c==3):
        mult()
    elif(c==4):
        div()
    else:
        print("Enter a valid number")
        main()
main()
def sum():
    n1=int(input("Enter number N1: "))
    n2=int(input("Enter number N2: "))
    sum=n1+n2
    print("Sum: ",sum)

def sub():
    n1=int(input("Enter number N1: "))
    n2=int(input("Enter number N2: "))
    sum=n1-n2
    print("Sum: ",sum)
    
def mult():
    n1=int(input("Enter number N1: "))
    n2=int(input("Enter number N2: "))
    sum=n1*n2
    print("Sum: ",sum)
    
def div():
    n1=int(input("Enter number N1: "))
    n2=int(input("Enter number N2: "))
    sum=n1/n2
    print("Sum: ",sum)