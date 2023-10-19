#Linear search
def search(list,ele):
    list2=[]
    flag=False
    for i in range (len(list)):
        if ele==list[i]:
            flage=True
            list2.append(i)
            
    if flag==True :
        for i in list2:
            print("Element",ele,"is found at position",i)
    else:
        print("Element not found")
        
list=[13,25.45,2,78,69,82,11,34,65]
ele=int(input("Enter the element to be serached: "))
print(search(list,ele))