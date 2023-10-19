#sum of positive integers
def sum(a):
    if(a<1):
        return 0
    else:
        return a+sum(a-2)
a=int(input("Enter number: "))
print(sum(a))