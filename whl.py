A=[10,4,5,7.30]

product=1

index=0
product *= A[index]


while index< len(A):
    print(A[index])
    index += 1

while index < len(A):
    product *= A[index]
    index += 1
print("product is", product) 

'''
print("PRIME NUMBER CHECKER")

print("______________________")

print("Enter the number")
n=(int(input()))

isdivisible= False
i=2
while i<n:
    if n % i== 0:
        isdivisible = True
        print("No. is divisible by {}", format(i))
    i+=1
if isdivisible:
    print(" This is not a prime number")
else:
    print("this is a prime number")'''



    