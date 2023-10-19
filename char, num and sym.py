#find char sym and num
cis=input("Enter element: ")

if(cis>='a' and cis<='z') or (cis>='A' and cis<='Z'):
    print("Character")
elif(cis>='0' or cis>='9'):
    print("Number")
else:
    print("Symbol")