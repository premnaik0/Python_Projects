#square of a number
class findsum:
    def square(self,a):
        s=a**a
        return s
    def cube(self,b):
        u=b*b*b
        return u
a=int(input("Enter number: "))
b=a

obj=findsum()
s=obj.square(a)
u=obj.cube(b)

print("Square: ",s)
print("Cube: ",u)