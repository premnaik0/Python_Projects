#To find the triangle
s1=int(input("Enter side 1:\n"))
s2=int(input("Enter side 2:\n"))
s3=int(input("Enter side 3:\n"))

if(s1==s2 and s1==s3):
    print("Equilateral triangle")
elif(s1!=s2 or s1!=s3):
    print("Isoceles triangle")
elif(s1==s2 or s1==s3):
    print("Scalere triangle")