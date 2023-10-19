#Revesing of number
n1=int(input("Enter n1 number\n"))
r=0
while(n1>0):
    s=n1%10
    r=(r*10)+s
    n1=n1//10
print(r)