#to print month and number of days in month
month=input("Enter a month to find days in it: ")

if(month=='january' or month=='January' or month=='march' or month=='March' or month=='may' or month=='May'or month=='july' or month=='July' or month=='august' or month=='August' or month=='october' or month=='October' or month=='december' or month=='December'):
    print(month,"has 31 day")
elif(month=='febuary' or month=='Febuary'):
    print(month,"28/29 days")
elif(month=='april' or month=='April' or month=='june' or month=='June' or month=='september' or month=='September' or month=='november' or month=='november'):
    print(month,"has 30 days")
else:
    print("Please enter a valid month")