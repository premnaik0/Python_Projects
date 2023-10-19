#Percentage
i=1
s=0

while(i<=5):
    m=float(input("Enter marks for out of 100: "))
    s=s+m
    i+=1
    
p=s/500*100
print("Total: ",s)
print("Percentage: ",p)

if(p>=40):
    print("PASS")
else:
    print("FAIL")