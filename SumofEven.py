n1 = int(input("enter the number"))
n2 = int(input("enter the number"))
sum = 0
for i in range (n1 , n2+1 ):
    if(i % 2 ==0):
        sum += i
print(sum)
