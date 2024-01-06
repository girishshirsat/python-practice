print("Enter number")
n=int(input())

if (n>0):
    print("Number is Accepted")
else:
    print("No is not accepted")    
    
    
print("_____________________________________________________________________")
i=0
print("Enter numbers")
for i in range(3):
    n=int(input())
    print("YOUR ENTRIES:",n)

print("Enter No.1")
a=int(input())
print("Enter No.1")
b=int(input())
print("Enter No.1")
c=int(input())

if (a>b and a>c):
    print("A is greater")
elif (b>a and b>c):
    print("b is greater")
else:
    print("c is greater")