#check whether year is leap year or not

year = int(input("Enter the year"))
if(year%4==0) or (year % 400 == 0 and year %100 != 0) :
    print("Leap Year")
else:
    print("Not a Leap Year")
