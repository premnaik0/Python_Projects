#leap
def leap():
    y=int(input("Enter year: "))
    
    if(y%4==0):
        print("Leap year")
        leap()
    else:
        print("Not a Leap year")
leap()