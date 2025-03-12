n = int(input("Enter the number"))
strong = 0
temp = n
while(n!=0):
    rem = n % 10
    tempfact = 1
    for i in range(1,rem+1):
        tempfact = tempfact * i
    strong += tempfact
    n=n//10
if(strong == temp):
    print("Strong number")
else:
    print("Not a Strong Number")
    
    
