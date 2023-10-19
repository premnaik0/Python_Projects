#classes in python
class findsum:
    def sum(self,a,b):
        s=a+b
        return s
a=int(input("Enter number 1: "))
b=int(input("Enter number 2: "))

obj=findsum()
s=obj.sum(a,b)

print("Sum: ",s)