a = int(input("enter the number"))
b = int(input("enter the number"))
c = int(input("enter the number"))

if(a>b and a>c):
    greatest = a
elif (b>a and b>c):
    greatest = b
else:
    greatest = c
print(greatest)
