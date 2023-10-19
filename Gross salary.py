#gross salary
n=float(input("Enter your basic salary: "))
hra=0
da=0
if(n<10,000):
    hra=n*20/100
    da=n*80/100
    gs=n+hra+da
    print(gs)
elif(n<=20,000):
    hra=n*25/100
    da=n*90/100
    gs=n+hra+da
    print(gs)
else:
    hra=n*30/100
    da=n*95/100
    gs=n+hra+da
    print(gs)