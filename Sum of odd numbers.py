#Sum of odd numbers
i=1
sum=0
while (i<=10):
    if(i%2==0):
        i+=1
        continue
    else:
        sum=sum+i
        i+=1
print(sum)