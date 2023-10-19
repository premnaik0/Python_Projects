num=int(input("enter a number"))
r=0
x=num
while(num>0):
    s=num%10
    r=(r*10)+s
    num=num//10
if(x==r):
    print("this is a palindrome")
else:
    print("this is not a palindrome")