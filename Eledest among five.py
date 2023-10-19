#eledest among five
n1=int(input("Enter age of person1:\t"))
n2=int(input("Enter age of person2:\t"))
n3=int(input("Enter age of person3:\t"))
n4=int(input("Enter age of person4:\t"))
n5=int(input("Enter age of person5:\t"))

if(n1>n2 and n1>n3 and n1>n4 and n1>n5):
    print("Person1 is eldest among all five people")
elif(n2>n1 and n2>n3 and n2>n4 and n2>n5):
    print("Person2 is eldest among all five people")
elif(n3>n1 and n3>n2 and n3>n4 and n3>n5):
    print("Person3 is eldest among all five people")
elif(n4>n1 and n4>n3 and n4>n2 and n4>n5):
    print("Person4 is eldest among all five people")
else:
    print("Person5 is eldest among all five people")
