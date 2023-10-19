#display decending numbers
def des(n):
    if(n==1):
        return 1
    elif(n==0):
        return 0
    else:
        return n,des(n-1)
n=int(input("Enter number: "))
print(des(n))