#find sum of all numbers
def sum(start,end):
    result=0
    for i in range(start,end+1):
        result=result+i
    print(result) 
sum(10,20)