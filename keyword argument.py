#keyword argument
def student(firstname, lastname="Mark", standerd="5th"):
    print(firstname,lastname,"studies in",standerd,"standerd")
    
#arg1
student(firstname="John")

#arg2
student(firstname="John",standerd="7th")

#arg2
student(lastname="Gates",firstname="John")